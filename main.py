import random


def create_garden(row, col):
    """Return a Grid for the Garden with n by m squares and 4 flowers and 3 weedss ."""

    garden = [["." for _ in range(col)] for _ in range(row)]

    for _ in range(4):
        while True:
            coordi_flower_x = random.randint(0, row - 1)
            coordi_flower_y = random.randint(0, col - 1)
            if garden[coordi_flower_x][coordi_flower_y] == ".":
                garden[coordi_flower_x][coordi_flower_y] = "F"
                break

    # Generate random integers 3 times for placement of the minimum 3 weeds
    for _ in range(3):
        while True:
            coordi_weed_x = random.randint(0, row - 1)
            coordi_weed_y = random.randint(0, col - 1)
            if garden[coordi_weed_x][coordi_weed_y] == ".":
                garden[coordi_weed_x][coordi_weed_y] = "W"
                break

    # Loop for 1/10 chance of every square being either a flower or Weed
    for r in range(row):
        for c in range(col):
            roulette = random.randint(1, 10)
            if roulette == 1:
                random_fifty = random.randint(1, 2)
                if random_fifty == 1:
                    garden[r][c] = "F"
                elif random_fifty == 2:
                    garden[r][c] = "W"

    return garden


# function to display the garden


def display_garden(garden, horizontal, vertical):
    for r in range(horizontal):
        for c in range(vertical):
            print(garden[r][c], end="")
        print("")


# functions for spreadment if the square is empty


def spread_up(garden, coordi_spread_x, coordi_spread_y, item):
    try:
        if garden[coordi_spread_x - 1][coordi_spread_y] == ".":
            garden[coordi_spread_x - 1][coordi_spread_y] = item
    except IndexError:
        pass  # If IndexError occurs, do nothing (implicitly return garden)
    return garden


def spread_right(garden, coordi_spread_x, coordi_spread_y, item):
    try:
        if garden[coordi_spread_x][coordi_spread_y + 1] == ".":
            garden[coordi_spread_x][coordi_spread_y + 1] = item
    except IndexError:
        pass  # If IndexError occurs, do nothing (implicitly return garden)
    return garden


def spread_left(garden, coordi_spread_x, coordi_spread_y, item):
    try:
        if garden[coordi_spread_x][coordi_spread_y - 1] == ".":
            garden[coordi_spread_x][coordi_spread_y - 1] = item
    except IndexError:
        pass  # If IndexError occurs, do nothing (implicitly return garden)
    return garden


def spread_down(garden, coordi_spread_x, coordi_spread_y, item):
    try:
        if garden[coordi_spread_x + 1][coordi_spread_y] == ".":
            garden[coordi_spread_x + 1][coordi_spread_y] = item
    except IndexError:
        pass  # If IndexError occurs, do nothing (implicitly return garden)
    return garden


# counts the total number of flowers and weeds
def counting_items(garden, horizontal, vertical):
    flower_count = 0
    weed_count = 0
    for rows in range(horizontal):
        for column in range(vertical):
            if garden[rows][column] == "F":
                flower_count += 1
            elif garden[rows][column] == "W":
                weed_count += 1
    return flower_count, weed_count


# Ensures fulfillment of condittions with eachh passing day in the simulation where each flower and weed takes over adjacent squares


def day_increment(garden, horizontal, vertical):
    for row in range(horizontal):
        for col in range(vertical):
            if garden[row][col] == "F":
                item = "F"
                garden = spread_up(garden, row, col, item)
                garden = spread_down(garden, row, col, item)
                garden = spread_right(garden, row, col, item)
                garden = spread_left(garden, row, col, item)
            elif garden[row][col] == "W":
                item = "W"
                garden = spread_up(garden, row, col, item)
                garden = spread_down(garden, row, col, item)
                garden = spread_right(garden, row, col, item)
                garden = spread_left(garden, row, col, item)

    return garden


def main():

    horizontal = int(input("Enter the number of rows in the garden: "))
    vertical = int(input("Enter the number of columns in the garden: "))

    # call make and display garden functions
    garden = create_garden(horizontal, vertical)
    display_garden(garden, horizontal, vertical)
    cont = True
    while cont:
        # main code

        # ask the user choice menu
        choice = int(
            input(
                "What do you want to do? Plant,remove weeds, or count the number of plants and weeds. Enter 1, 2, 3: press 4 for passing N days "
            )
        )

        if choice == 1:
            x = int(input("Enter the x coordinate for where you want to plant: ")) - 1
            y = int(input("Enter the y coordinate for where you want to plant: ")) - 1
            if garden[x][y] != ".":
                print("Invalid, item already present in that area.")
            else:
                garden[x][y] = "F"
            display_garden(garden, horizontal, vertical)

        elif choice == 2:
            x = (
                int(input("enter the x coordinate form where you want to remove weed "))
                - 1
            )
            y = (
                int(
                    input(
                        "Enter the ycoordinate form where you want ot remove weed :  "
                    )
                )
                - 1
            )
            if garden[x][y] != "W":
                print("Invalid, no weed in the area.")
            else:
                garden[x][y] = "."

            display_garden(garden, horizontal, vertical)

        elif choice == 4:
            days = int(input("How many days do you want to simulate? "))

            for _ in range(days):
                garden = day_increment(
                    garden, horizontal, vertical
                )  # Update garden with the latest state
                print()
                print("----------")
                print()
                display_garden(garden, horizontal, vertical)

        elif choice == 3:
            flower_num, weed_num = counting_items(garden, horizontal, vertical)
            print(f"The number of flowers are {flower_num}")
            print(f"The number of weeds are {weed_num}")

        continue_ = str(input("Do you want to continue? y or n: ")).lower()
        if continue_ == "y":
            cont = True
            continue
        else:
            cont = False


main()
