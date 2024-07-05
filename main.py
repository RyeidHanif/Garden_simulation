import random

EMPTY_CELL = "."
FLOWER = "F"
WEED = "W"

def plant_random(garden , amount , item , row , col):
    for i in range(amount):
        while True : 
            coordi_flower_x = random.randint(0, row - 1)
            coordi_flower_y = random.randint(0, col - 1)
            if garden[coordi_flower_x][coordi_flower_y] == EMPTY_CELL:
                garden[coordi_flower_x][coordi_flower_y] = item
                break
    return garden
        


def create_garden(row, col):
    """Return a Grid for the Garden with n by m squares and 4 flowers and 3 weedss ."""
    garden = []

    for r in range(row):  
        rows = []  
        for c in range(col):  
            cell_value = EMPTY_CELL  
            roulette = random.randint(1, 10)  
            if roulette == 1:  
                random_fifty = random.randint(1, 2)  
                if random_fifty == 1:  
                    cell_value = FLOWER  
                elif random_fifty == 2:  
                    cell_value = WEED  
            rows.append(cell_value)  
        garden.append(rows) 
    
    plant_random(garden , 4 , FLOWER , row , col)
    plant_random(garden , 3 ,WEED ,  row , col)
    
    return garden


# function to display the garden


def display_garden(garden, horizontal, vertical):
    """Return a grid of n by m squares"""
    for r in range(horizontal):
        for c in range(vertical):
            print(garden[r][c], end="")
        print("")





# counts the total number of flowers and weeds
def counting_items(garden, horizontal, vertical):
    """Return the number of flowers and weeds in the garden"""
    flower_count = 0
    weed_count = 0
    for rows in range(horizontal):
        for column in range(vertical):
            if garden[rows][column] == FLOWER:
                flower_count += 1
            elif garden[rows][column] == WEED:
                weed_count += 1
    return flower_count, weed_count


# Ensures fulfillment of condittions with eachh passing day in the simulation where each flower and weed takes over adjacent squares

def plant(garden ,coordi_spread_x , coordi_spread_y , item):
    try:
        if garden[coordi_spread_x ][coordi_spread_y] == EMPTY_CELL:
           garden[coordi_spread_x][coordi_spread_y] = item
    except IndexError :
        pass 
    return garden



def day_increment(garden, horizontal, vertical):
    """Returns a version of the garden where a day has passed"""
    

    # return garden
    
    for row in range(horizontal):
        for col in range(vertical):
            item = garden[row][col]
            plant(garden, row - 1, col , item)
            plant(garden, row + 1, col , item)
            plant(garden, row, col - 1 , item)
            plant(garden ,row, col + 1,item)
            

    
    return garden

def grow_garden(garden , horizontal , vertical):
    days = int(input("How many days do you want to simulate? "))

    for _ in range(days):
        garden = day_increment(
            garden, horizontal, vertical
        )  # Update garden with the latest state
        
        print("\n----------\n")
        
        display_garden(garden, horizontal, vertical)

def input_coordi(horizontal , vertical):
    x = int(input('Enter the row number'))
    y = int(input("Enter the column numbers"))
    while x > horizontal or y > vertical  or x < 0 or y < 0 :
        print("either your row or column number is invalid")
        x = int(input('Enter the row number'))
        y = int(input("Enter the column numbers"))
    
    return x-1 , y-1



   

if __name__ == "__main__":
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

            x, y = input_coordi(horizontal , vertical)
        
            if garden[x][y] != EMPTY_CELL:
                print("Invalid, item already present in that area.")
            else:
                garden[x][y] = FLOWER
            display_garden(garden, horizontal, vertical)

        elif choice == 2:
            x, y = input_coordi(horizontal , vertical)
            if garden[x][y] != WEED:
                print("Invalid, no weed in the area.")
            else:
                garden[x][y] = EMPTY_CELL

            display_garden(garden, horizontal, vertical)

        elif choice == 4:
            grow_garden(garden, horizontal, vertical)

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


