# Exercise: Work with arguments in functions
# Required arguments in functions are used when functions need those arguments to work properly. In this exercise, you'll construct a fuel report that requires information from several fuel locations throughout the rocket ship.

# This exercise is broken into a series of steps. For each step you will be presented with the goal for the step, followed by an empty cell. Enter your Python into the cell and run it. The solution for each step will follow each cell.

# # Create a report generation function
# # Your spaceship has three tanks: Main, External and Hydrogen. You want to create an app to display the amount of fuel in each tank, and the average amount of fuel between the three tanks. Because you wish to reuse this code in other projects, you want to create a function with the logic.

# # Create a function named generate_report. The function will take three parameters named main_tank, external_tank and hydrogen_tank. When run, the function will display output which resembles the following:

def generate_report(main_tank, external_tank,hydrogen_tank):
    output = f"""
    Main tank: {main_tank}
    External tank: {external_tank}
    Hydrogen tank: {hydrogen_tank}
    """

    print(output)

generate_report(80,70,75)
