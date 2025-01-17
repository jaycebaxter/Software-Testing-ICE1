###############################################################
# Program: Movie Budget Calculator
# Author: Jayce Baxter
# Date: January 14th, 2025
# Description: Calculates the average budget of several movies
###############################################################

# Initializing variables that I will need to use
movies_num = ""
movies_num_validation = False
budget_validation = False
menu_option = False
user_exit = False

# Initializing my lists
movies = []
budgets = []

# Turning this into a function so I don't have to type it twice
def add_movies():

    movies_num_validation = False

    # Prompting the user for number of movies they are adding to the list
    global movies_num
    movies_num = input("How many movies would you like to add? ")

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

        # Prints an error if validation does not pass, prompts the user again
        except:
            print("Please enter a whole, positive number. \n")
            movies_num = input("How many movies would you like to add? ")

    # Begins a for loop that runs one iteration for every movie the user wishes to add
    for i in range(int(movies_num)):

        # Sets budget_validation to false every loop
        budget_validation = False

        # Prompts the user to input the title of a movie and appends to the movies list
        new_movie = input("Please input the movie's title: ")
        movies.append(new_movie)

        # Using a while loop to ensure budget is numeric
        while budget_validation == False:

            # Prompts the user to enter the movie's budget and appends to the budgets list if validation passes
            new_budget = input("Please input the movie's budget: $")

            # Tries to convert the budget to a float, verifying that it is a number.
            try:
                new_budget = float(new_budget)
                if new_budget > 0:
                    budgets.append(new_budget)
                    budget_validation = True
                
            # Prints an error message if the budget is not numeric, prompts the user again
            except:
                print("Please enter a positive number.")
                continue

add_movies()

while True:
    menu_option = input("\nPress 1 to calculate, 2 to add more movies, or 3 to exit --> ")

    if menu_option == "1":
        # budgets = list(map(int, budgets))
        average = sum(budgets) / int(movies_num)
        print(f"The average of all movie budgets is {round(average,2)}.")
        

    elif menu_option == "2":
        add_movies()
        
    elif menu_option == "3":
        print("Exiting program")
        exit()


