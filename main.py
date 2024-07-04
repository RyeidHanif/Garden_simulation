import random

# Create the Garden 2D array


def create_garden(row, col):
    garden = [["." for _ in range(col)] for _ in range(row)]

    # Generate 4 random pairs of integers for the placement of 4 flowers in the original map
    for _ in range(4):
        coordi_flower_x = random.randint(0, row - 1)
        coordi_flower_y = random.randint(0, col - 1)
        if garden[coordi_flower_x][coordi_flower_y] == ".":
            garden[coordi_flower_x][coordi_flower_y] = "F"
        else:
            while garden[coordi_flower_x][coordi_flower_y] != ".":
                coordi_flower_x = random.randint(0, row - 1)
                coordi_flower_y = random.randint(0, col - 1)
            garden[coordi_flower_x][coordi_flower_y] = "F"

    # generate random integers 3 times for placement of the minimum 3 weeds
    for _ in range(3):
        coordi_weed_x = random.randint(0, row - 1)
        coordi_weed_y = random.randint(0, col - 1)
        if garden[coordi_weed_x][coordi_weed_y] == ".":
            garden[coordi_weed_x][coordi_weed_y] = "W"
        else:
            while garden[coordi_weed_x][coordi_weed_y] != ".":
                coordi_weed_x = random.randint(0, row - 1)
                coordi_weed_y = random.randint(0, col - 1)
            garden[coordi_weed_x][coordi_weed_y] = "W"

    # Loop for 1/10 chance of every square being either a flower or Weed
    for r in range(row):
        for c in range(col):
            roulette = random.randint(1, 10)
            if roulette == 1:
                garden[r][c] = "F"
            elif roulette == 5:
                garden[r][c] = "W"
            else:
                pass

    return garden


# function to display the garden


def display_garden(garden, horizontal, vertical):
    for r in range(horizontal):
        for c in range(vertical):
            print(garden[r][c], end="")
        print("")


# functions for movement if the square is empty


def move_up(garden, coordi_move_x, coordi_move_y, item):
    if garden[coordi_move_x - 1][coordi_move_y] == ".":
        garden[coordi_move_x - 1][coordi_move_y] = item
        return garden
    return garden


def move_down(garden, coordi_move_x, coordi_move_y, item):
    if garden[coordi_move_x + 1][coordi_move_y] == ".":
        garden[coordi_move_x + 1][coordi_move_y] = item
        return garden
    return garden


def move_right(garden, coordi_move_x, coordi_move_y, item):

    if garden[coordi_move_x][coordi_move_y + 1] == ".":

        garden[coordi_move_x][coordi_move_y + 1] = item
        return garden
    return garden


def move_left(garden, coordi_move_x, coordi_move_y, item):
    if garden[coordi_move_x][coordi_move_y - 1] == ".":
        garden[coordi_move_x][coordi_move_y - 1] = item
        return garden
    return garden


# counts the total number of flowers and weeds
def counting_items(garden):
    flower_count = 0
    weed_count = 0
    for rows in garden:
        for column in rows:
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
                if row != 0 and col != 0 and row != horizontal and col != vertical:
                    move_up(garden, row, col, item)
                    move_down(garden, row, col, item)
                    move_right(garden, row, col, item)
                    move_left(garden, row, col, item)

                elif row == 0:
                    move_down(garden, row, col, item)
                    move_right(garden, row, col, item)
                    move_left(garden, row, col, item)

                elif col == 0:
                    move_up(garden, row, col, item)
                    move_down(garden, row, col, item)
                    move_right(garden, row, col, item)

                elif row == horizontal:
                    move_up(garden, row, col, item)
                    move_right(garden, row, col, item)
                    move_left(garden, row, col, item)

                elif col == vertical:
                    move_up(garden, row, col, item)
                    move_down(garden, row, col, item)
                    move_left(garden, row, col, item)

                elif row == 0 and col == 0:
                    move_down(garden, row, col, item)
                    move_right(garden, row, col, item)

                elif row == horizontal and col == vertical:
                    move_up(garden, row, col, item)
                    move_left(garden, row, col, item)

                elif row == 0 and col == vertical:
                    move_down(garden, row, col, item)
                    move_left(garden, row, col, item)

                elif row == horizontal and col == 0:
                    move_up(garden, row, col, item)
                    move_right(garden, row, col, item)

                return garden
            elif garden[row][col] == "F":
                item = "F"

                if row != 0 and col != 0 and row != horizontal and col != vertical:
                    move_up(garden, row, col, item)
                    move_down(garden, row, col, item)
                    move_right(garden, row, col, item)
                    move_left(garden, row, col, item)

                elif row == 0:
                    move_down(garden, row, col, item)
                    move_right(garden, row, col, item)
                    move_left(garden, row, col, item)

                elif col == 0:
                    move_up(garden, row, col, item)
                    move_down(garden, row, col, item)
                    move_right(garden, row, col, item)

                elif row == horizontal:
                    move_up(garden, row, col, item)
                    move_right(garden, row, col, item)
                    move_left(garden, row, col, item)

                elif col == vertical:
                    move_up(garden, row, col, item)
                    move_down(garden, row, col, item)
                    move_left(garden, row, col, item)

                elif row == 0 and col == 0:
                    move_down(garden, row, col, item)
                    move_right(garden, row, col, item)

                elif row == horizontal and col == vertical:
                    move_up(garden, row, col, item)
                    move_left(garden, row, col, item)

                elif row == 0 and col == vertical:
                    move_down(garden, row, col, item)
                    move_left(garden, row, col, item)

                elif row == horizontal and col == 0:
                    move_up(garden, row, col, item)
                    move_right(garden, row, col, item)
                return garden
    return garden


cont = True
while cont:
    # main code
    horizontal = int(input("Enter the number of rows in the garden: "))
    vertical = int(input("Enter the number of columns in the garden: "))

    # call make and display garden functions
    garden = create_garden(horizontal, vertical)
    display_garden(garden, horizontal, vertical)

    # ask the user choice menu
    choice = int(
        input(
            "What do you want to do? Plant, Remove, Pass n Days or count the number of plants and weeds. Enter 1, 2, 3 or 4: "
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
        x = int(input("Enter the x coordinate for where you want to remove: ")) - 1
        y = int(input("Enter the y coordinate for where you want to remove: ")) - 1
        if garden[x][y] != "W":
            print("Invalid, no weed in the area.")
        else:
            garden[x][y] = "."

        display_garden(garden, horizontal, vertical)

    elif choice == 3:
        days = int(input("How many days do you want to simulate? "))

        for _ in range(days):
            garden = day_increment(
                garden, horizontal, vertical
            )  # Update garden with the latest state
            print()
            print("----------")
            print()
            display_garden(garden, horizontal, vertical)

    elif choice == 4:
        flower_num, weed_num = counting_items(garden)
        print(f"The number of flowers are {flower_num}")
        print(f"The number of weeds are {weed_num}")

    continue_ = str(input("Do you want to continue? y or n: ")).lower()
    if continue_ == "y":
        cont = True
        continue
    else:
        cont = False
