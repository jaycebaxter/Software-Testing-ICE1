###############################################################
# Program: Movie Budget Calculator
# Author: Jayce Baxter
# Date: January 14th, 2025
# Description: Calculates the average budget of several movies
###############################################################

# Initializing variables that I will need to use
movies_num = ""
movies_num_validation = False

# Prompting the user for number of movies they are adding to the list
movies_num = input("How many movies would you like to add? ")

# Initializing a while loop that defaults to false until validation passes
while movies_num_validation == False:

    # Tries to convert movies_num to an integer, and changes movies_num_validation to True if it passes
    try:
        int(movies_num)
        if movies_num.isnumeric():
            movies_num_validation = True

    # Prints an error if validation does not pass, prompts the user again
    except:
        print("Please enter a whole number. \n")
        movies_num = input("How many movies would you like to add? ")

# Initializing my lists
movies = []
budgets = []

# Begins a for loop that runs one iteration for every movie the user wishes to add
for i in range(int(movies_num)):

    # Prompts the user to input the title of a movie and appends to the movies list
    new_movie = input("Please input the movie's title: ")
    movies.append(new_movie)

    # Prompts the user to enter the movie's budget and appends to the budgets list if validation passes
    new_budget = input("Please input the movie's budget: $")

    # Tries to convert the budget to a float, verifying that it is a number.
    try:
        float(new_budget)
        budgets.append(new_budget)

    # Prints an error message if the budget is not numeric, prompts the user again
    except:
        print("Please enter a number.")
        new_budget = input("Please input the movie's budget: $")

print(movies)
print(budgets)
