# Pratik Sanjay Belhekar
# Part 1 : Problem 2
# python 2.7

width = int(raw_input("Width: "))
height = int(raw_input("Height: "))
intialChar = raw_input("Initial Character: ")

def world_initializer(width , height , ic = " "):
    if len(ic) >= 2 :
        return None
    else:
        fgame_list = [[ic for  w in range(width)] for h in range(height)]
        return fgame_list


if intialChar == ' ':
    game_list = world_initializer(width, height)
    print game_list
else:
    game_list = world_initializer(width, height, intialChar)
    print game_list