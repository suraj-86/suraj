import sqlite3
from flask import Flask, render_template, request, redirect, url_for, flash, session
import random
import string
from functools import wraps # Required for the admin decorator

app = Flask(__name__)
app.secret_key = 'your_very_secret_key_change_this'

#Database Setup
def init_db():
    conn = sqlite3.connect('database.db')
    conn.execute('''CREATE TABLE IF NOT EXISTS users (
                    username TEXT PRIMARY KEY, 
                    password TEXT, 
                    full_name TEXT,
                    email TEXT,
                    phone TEXT,
                    dob TEXT,
                    address TEXT, 
                    profile_pic_url TEXT,
                    is_admin BOOLEAN DEFAULT 0
                )''')
    conn.execute('CREATE TABLE IF NOT EXISTS bookings (pnr TEXT PRIMARY KEY, username TEXT, passenger_name TEXT, train_name TEXT, travel_date TEXT)')
    conn.execute('CREATE TABLE IF NOT EXISTS trains (id INTEGER PRIMARY KEY AUTOINCREMENT, train_name TEXT, origin TEXT, destination TEXT, departure_time TEXT, running_days TEXT)')
    conn.close()

def seed_data():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    # Seed admin user
    cursor.execute("SELECT COUNT(*) FROM users WHERE username = 'admin'")
    if cursor.fetchone()[0] == 0:
        print("Creating admin user...")
        cursor.execute("INSERT INTO users (username, password, is_admin) VALUES (?, ?, ?)", ('admin', 'admin8676', 1))
        conn.commit()

    # Seed trains
    cursor.execute("SELECT COUNT(*) FROM trains")
    if cursor.fetchone()[0] == 0:
        print("Seeding trains...")
        trains_data = [('Shatabdi Express', 'New Delhi', 'Lucknow', '06:15', 'Daily'), ('Rajdhani Express', 'Mumbai', 'New Delhi', '17:00', 'Daily'), ('Duronto Express', 'Kolkata', 'Pune', '05:45', 'Mon, Wed, Sat'), ('Tejas Express', 'Chennai', 'Madurai', '06:00', 'Daily except Thu')]
        cursor.executemany("INSERT INTO trains (train_name, origin, destination, departure_time, running_days) VALUES (?, ?, ?, ?, ?)", trains_data)
        conn.commit()
    conn.close()

init_db()
seed_data()

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            flash('Please log in to access this page.', 'error')
            return redirect(url_for('login'))
        
        conn = sqlite3.connect('database.db')
        conn.row_factory = sqlite3.Row
        user = conn.execute('SELECT * FROM users WHERE username = ?', (session['username'],)).fetchone()
        conn.close()

        if not user or not user['is_admin']:
            flash('You do not have permission to access the admin panel.', 'error')
            return redirect(url_for('home'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = sqlite3.connect('database.db')
        conn.row_factory = sqlite3.Row
        user = conn.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password)).fetchone()
        conn.close()
        if user:
            session['username'] = username
            session['is_admin'] = user['is_admin']
            flash('You were successfully logged in!', 'success')
            return redirect(url_for('home'))
        else:
            error = 'Invalid credentials. Please try again.'
            flash(error, 'error')
    return render_template('login.html', error=error)

@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = sqlite3.connect('database.db')
        try:
            conn.execute('INSERT INTO users (username, password, is_admin) VALUES (?, ?, ?)', (username, password, 0)) # Regular users are not admin
            conn.commit()
            flash('Registration successful! Please login.', 'success')
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            error = 'Username already exists.'
            flash(error, 'error')
        finally:
            conn.close()
    return render_template('register.html', error=error)

@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('is_admin', None)
    flash('You have been logged out.', 'success')
    return redirect(url_for('home'))

@app.route('/book', methods=['GET', 'POST'])
def book_ticket():
    if 'username' not in session:
        flash('You need to be logged in to book a ticket.', 'error')
        return redirect(url_for('login'))
    
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    trains = conn.execute('SELECT train_name, origin, destination FROM trains').fetchall()
    
    if request.method == 'POST':
        passenger_name = request.form['passenger_name']
        train_name = request.form['train_name']
        travel_date = request.form['travel_date']
        pnr = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
        conn.execute('INSERT INTO bookings (pnr, username, passenger_name, train_name, travel_date) VALUES (?, ?, ?, ?, ?)',
                     (pnr, session['username'], passenger_name, train_name, travel_date))
        conn.commit()
        flash(f'Ticket booked successfully! Your PNR is {pnr}', 'success')
        conn.close()
        return redirect(url_for('my_bookings'))
        
    conn.close()
    return render_template('booking.html', trains=trains)

@app.route('/my_bookings')
def my_bookings():
    if 'username' not in session:
        flash('You need to be logged in to view your bookings.', 'error')
        return redirect(url_for('login'))

    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    bookings = conn.execute('''
        SELECT b.pnr, b.passenger_name, b.train_name, b.travel_date, t.departure_time 
        FROM bookings b JOIN trains t ON b.train_name = t.train_name 
        WHERE b.username = ?
    ''', (session['username'],)).fetchall()
    conn.close()
    
    return render_template('my_bookings.html', bookings=bookings)

@app.route('/cancel_booking/<string:pnr>', methods=['POST'])
def cancel_booking(pnr):
    if 'username' not in session:
        flash('Please log in to manage your bookings.', 'error')
        return redirect(url_for('login'))

    conn = sqlite3.connect('database.db')
    conn.execute('DELETE FROM bookings WHERE pnr = ? AND username = ?', (pnr, session['username']))
    conn.commit()
    conn.close()

    flash(f'Your booking for PNR {pnr} has been successfully cancelled.', 'success')
    return redirect(url_for('my_bookings'))

@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if 'username' not in session:
        flash('Please log in to view your profile.', 'error')
        return redirect(url_for('login'))

    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    
    if request.method == 'POST':
        full_name = request.form['full_name']
        email = request.form['email']
        phone = request.form['phone']
        dob = request.form['dob']
        address = request.form['address']
        profile_pic_url = request.form['profile_pic_url']
        
        conn.execute('''UPDATE users SET 
                        full_name = ?, email = ?, phone = ?, dob = ?, address = ?, profile_pic_url = ? 
                        WHERE username = ?''',
                     (full_name, email, phone, dob, address, profile_pic_url, session['username']))
        conn.commit()
        flash('Your profile has been updated successfully!', 'success')
        conn.close()
        return redirect(url_for('profile'))

    user = conn.execute('SELECT * FROM users WHERE username = ?', (session['username'],)).fetchone()
    conn.close()
    
    if not user:
        session.pop('username', None)
        session.pop('is_admin', None)
        flash('Your session was invalid. Please log in again.', 'error')
        return redirect(url_for('login'))
    
    edit_mode = request.args.get('edit', 'false').lower() == 'true'
    return render_template('profile.html', user=user, edit_mode=edit_mode)

@app.route('/change_password', methods=['GET', 'POST'])
def change_password():
    if 'username' not in session:
        flash('Please log in to change your password.', 'error')
        return redirect(url_for('login'))

    if request.method == 'POST':
        current_password = request.form['current_password']
        new_password = request.form['new_password']
        confirm_password = request.form['confirm_password']
        
        conn = sqlite3.connect('database.db')
        conn.row_factory = sqlite3.Row
        user = conn.execute('SELECT * FROM users WHERE username = ?', (session['username'],)).fetchone()
        
        if not user:
            session.pop('username', None)
            session.pop('is_admin', None)
            flash('Your session has expired. Please log in again.', 'error')
            conn.close()
            return redirect(url_for('login'))
        elif user['password'] != current_password:
            flash('Incorrect current password.', 'error')
        elif new_password != confirm_password:
            flash('New passwords do not match.', 'error')
        else:
            conn.execute('UPDATE users SET password = ? WHERE username = ?', (new_password, session['username']))
            conn.commit()
            flash('Your password has been changed successfully.', 'success')
        
        conn.close()
        return redirect(url_for('change_password'))

    return render_template('change_password.html')

@app.route('/schedule')
def schedule():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    
    search_origin = request.args.get('origin', '')
    search_destination = request.args.get('destination', '')
    
    origins = conn.execute('SELECT DISTINCT origin FROM trains ORDER BY origin').fetchall()
    destinations = conn.execute('SELECT DISTINCT destination FROM trains ORDER BY destination').fetchall()
    
    query = "SELECT * FROM trains WHERE 1=1"
    params = []
    
    if search_origin:
        query += " AND origin = ?"
        params.append(search_origin)
    if search_destination:
        query += " AND destination = ?"
        params.append(search_destination)
        
    query += " ORDER BY train_name"
    
    trains = conn.execute(query, params).fetchall()
    conn.close()
    
    return render_template('schedule.html', 
                           trains=trains, 
                           origins=origins, 
                           destinations=destinations,
                           search_origin=search_origin, 
                           search_destination=search_destination)

@app.route('/pnr_status', methods=['GET', 'POST'])
def pnr_status():
    status = None
    if request.method == 'POST':
        pnr_to_check = request.form['pnr']
        conn = sqlite3.connect('database.db')
        booking = conn.execute('SELECT passenger_name, train_name FROM bookings WHERE pnr = ?', (pnr_to_check,)).fetchone()
        conn.close()
        if booking:
            status = {'found': True, 'pnr': pnr_to_check, 'passenger_name': booking[0], 'train_name': booking[1]}
        else:
            status = {'found': False, 'pnr': pnr_to_check}
    return render_template('pnr.html', status=status)

#admin

@app.route('/admin')
@admin_required
def admin_dashboard():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    trains = conn.execute('SELECT * FROM trains ORDER BY train_name').fetchall()
    conn.close()
    return render_template('admin/dashboard.html', trains=trains)

@app.route('/admin/train/add', methods=['GET', 'POST'])
@admin_required
def add_train():
    if request.method == 'POST':
        train_name = request.form['train_name']
        origin = request.form['origin']
        destination = request.form['destination']
        departure_time = request.form['departure_time']
        running_days = request.form['running_days']
        
        conn = sqlite3.connect('database.db')
        conn.execute('INSERT INTO trains (train_name, origin, destination, departure_time, running_days) VALUES (?, ?, ?, ?, ?)',
                     (train_name, origin, destination, departure_time, running_days))
        conn.commit()
        conn.close()
        
        flash(f'Train "{train_name}" has been added successfully!', 'success')
        return redirect(url_for('admin_dashboard'))
        
    return render_template('admin/add_train.html')

@app.route('/admin/train/edit/<int:train_id>', methods=['GET', 'POST'])
@admin_required
def edit_train(train_id):
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    
    if request.method == 'POST':
        train_name = request.form['train_name']
        origin = request.form['origin']
        destination = request.form['destination']
        departure_time = request.form['departure_time']
        running_days = request.form['running_days']
        
        conn.execute('UPDATE trains SET train_name = ?, origin = ?, destination = ?, departure_time = ?, running_days = ? WHERE id = ?',
                     (train_name, origin, destination, departure_time, running_days, train_id))
        conn.commit()
        conn.close()
        
        flash(f'Train "{train_name}" has been updated successfully!', 'success')
        return redirect(url_for('admin_dashboard'))
    
    train = conn.execute('SELECT * FROM trains WHERE id = ?', (train_id,)).fetchone()
    conn.close()
    
    if train is None:
        flash('Train not found.', 'error')
        return redirect(url_for('admin_dashboard'))
        
    return render_template('admin/edit_train.html', train=train)

@app.route('/admin/train/delete/<int:train_id>', methods=['POST'])
@admin_required
def delete_train(train_id):
    conn = sqlite3.connect('database.db')
    # Optional: Get train name before deleting for a better flash message
    train = conn.execute('SELECT train_name FROM trains WHERE id = ?', (train_id,)).fetchone()
    conn.execute('DELETE FROM trains WHERE id = ?', (train_id,))
    conn.commit()
    conn.close()
    
    flash(f'Train "{train[0] if train else "ID "+str(train_id)}" has been deleted.', 'success')
    return redirect(url_for('admin_dashboard'))

if __name__ == '__main__':
    app.run(debug=True)

