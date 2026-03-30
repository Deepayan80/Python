# Write a program to ask the user to enter names of their 3 favorite movies & store them in a list. Then, print the list.
movies = []
for i in range(3):
    movie = input("Enter the name of one of your favorite movies: ")
    movies.append(movie)
print("Your favorite movies are:", movies)