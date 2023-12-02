import re
f=open("day 2\input.txt", "r")
Lines = f.readlines()

RED_LIMIT = 12
GREEN_LIMIT = 13
BLUE_LIMIT = 14

def is_color_valid(color, limit):
    invalid_list = [x for x in color if int(x) > limit]
    if len(invalid_list) == 0:
        return True
    else:
        return False

gamelist = []
for line in Lines:
    red = re.findall("(\d+) red", line)
    green = re.findall("(\d+) green", line)
    blue = re.findall("(\d+) blue", line)
    game_id = re.findall("Game (\d+)", line)
    
    if is_color_valid(red, RED_LIMIT) == True and is_color_valid(green, GREEN_LIMIT) == True and is_color_valid(blue, BLUE_LIMIT) == True:
        gamelist += game_id

gamelist = list(map(lambda a : int(a), gamelist))

print(sum(gamelist))