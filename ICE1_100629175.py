###############################################################
# Program: Movie Budget Calculator
# Author: Jayce Baxter
# Date: January 14th, 2025
# Description: Calculates the average budget of several movies
###############################################################


movies_num = ""
movies_num_validation = False

movies_num = input("How many movies would you like to add? ")

while movies_num_validation == False:
    try:
        int(movies_num)
        if movies_num.isnumeric():
            movies_num_validation = True

    except:
        print("Please enter a whole number. \n")
        movies_num = input("How many movies would you like to add? ")

movies = []
budgets = []

for i in range(int(movies_num)):
    new_movie = input("Please input a movie: ")
    movies.append(new_movie)
    new_budget = input("Please input the movie's budget: ")
    budgets.append(new_budget)

