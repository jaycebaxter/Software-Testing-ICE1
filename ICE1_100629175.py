###############################################################
# Program: Movie Budget Calculator
# File: ICE_100629175.py
# Author: Jayce Baxter
# Date: January 14th, 2025
# Description: Calculates the average budget of several movies
###############################################################

# Creating the output log
output_log = open("output_log.txt", "w")

# Initializing variables that I will need to use
movies_num = ""
movies_num_validation = False
budget_validation = False
menu_option = False
user_exit = False

# Initializing my lists
movies = []
budgets = []
above_average_title = []
above_average_budget = []

# Turning this into a function so I don't have to type it twice
def add_movies():

    movies_num_validation = False

    # Prompting the user for number of movies they are adding to the list
    global movies_num
    movies_num = input("How many movies would you like to add? ")
    output_log.write(f"Number of movies: {movies_num}")

    # Initializing a while loop that defaults to false until validation passes
    while movies_num_validation == False:

        # Tries to convert movies_num to an integer, and changes movies_num_validation to True if it passes
        try:
            movies_num = int(movies_num)
            if movies_num >= 0:
                movies_num_validation = True

            else:
                print("Please enter a whole, positive number. \n")
                movies_num = input("How many movies would you like to add? ")
                output_log.write(f"Invalid user input. Number of movies: {movies_num}")

        # Prints an error if validation does not pass, prompts the user again
        except:
            print("Please enter a whole, positive number. \n")
            movies_num = input("How many movies would you like to add? ")
            output_log.write(f"Invalid user input. Number of movies: {movies_num}")


    # Begins a for loop that runs one iteration for every movie the user wishes to add
    for i in range(int(movies_num)):

        # Sets budget_validation to false every loop
        budget_validation = False

        # Prompts the user to input the title of a movie and appends to the movies list
        new_movie = input("Please input the movie's title: ")
        movies.append(new_movie)
        output_log.write(f"Name of movie: {new_movie}")

        # Using a while loop to ensure budget is numeric
        while budget_validation == False:

            # Prompts the user to enter the movie's budget and appends to the budgets list if validation passes
            new_budget = input("Please input the movie's budget: $")
            output_log.write(f"Movie's budget: {new_budget}")

            # Tries to convert the budget to a float, verifying that it is a number.
            try:
                new_budget = float(new_budget)
                if new_budget > 0:
                    budgets.append(new_budget)
                    budget_validation = True
                
            # Prints an error message if the budget is not numeric, prompts the user again
            except:
                print("Please enter a positive number.")
                output_log.write(f"Invalid user input.")
                continue

# Calling the function
add_movies()

# Giving the user menu options infinitely until they choose to exit
while True:
    menu_option = input("\nPress 1 to calculate, 2 to add more movies, or 3 to exit --> ")
    output_log.write(f"Menu option: {menu_option}")

# Calculations
    if menu_option == "1":

        # Calculating the average by taking the sum of all budgets and dividing by the number of movies
        total_movies = len(movies)
        average = sum(budgets) / total_movies
        print(f"\nThe average of all movie budgets is ${round(average,2)}.")
        output_log.write(f"Average budget: {round(average,2)}")

        # If the budget is higher than average, append the movie to "above average" list
        for i in range(total_movies):
            if budgets[i] > average:
                above_average_title.append(movies[i])
                above_average_budget.append(budgets[i])

        # Telling the user which movies are above average and by how much
        print("\nThe following movies had an above average budget:")
        output_log.write(f"Above average movies:")
        for i in range(len(above_average_title)):
            print(f"- {above_average_title[i]}: ${above_average_budget[i]} - Above average by ${round(above_average_budget[i] - average, 2)}")
            output_log.write(f"- {above_average_title[i]}: ${above_average_budget[i]} - Above average by ${round(above_average_budget[i] - average, 2)}")

        # Telling the user how many movies were above average
        print(f"\nThere were {len(above_average_title)} movies above average budget.")
        output_log.write(f"Movies with above average budget: {len(above_average_title)}")

        # Sorting the budgets and printing them from lowest to highest
        budgets.sort()
        print(f"\nBudgets from lowest to highest:")
        output_log.write("Budgets from lowest to highest:")
        for i in range(total_movies):
            print(f"$ {budgets[i]}")
            output_log.write(f"$ {budgets[i]}")

    # Giving the user the option to add more movies
    elif menu_option == "2":
        add_movies()
        
    # Exits
    elif menu_option == "3":
        print("Exiting program")
        output_log.write("Exiting program")
        exit()


