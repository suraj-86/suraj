# Input 20 integers from the keyboard

numbers = []

print("Enter 20 integers:")
for i in range(20):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

ascending = sorted(numbers)

descending = sorted(numbers, reverse=True)

print("\nNumbers in Ascending Order:")
for num in ascending:
    print(num, end=' ')

print("\n\nNumbers in Descending Order:")
for num in descending:
    print(num, end=' ')
