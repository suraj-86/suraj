#wap to enter names of three movies and store in a list

# a=list(str(input("enter your 3 favourite movies ")))
# print(a)

#method1
b=str(input("enter your favourite movie 1 : "))
c=str(input("enter your favourite movie 2 : "))
d=str(input("enter your favourite movie 3 : "))
a=[b,c,d]
print(a)

#method2

movies=[]

movie1=input("ether 1st movie name ")
movie2=input("ether 2nd movie name ")
movie3=input("ether 3rd movie name ")

movies.append(movie1)
movies.append(movie2)
movies.append(movie3)

print(movies)


#method3

movie=[]
movie.append(input("enter movie name "))
movie.append(input("enter movie name "))
movie.append(input("enter movie name "))
print(movie)
