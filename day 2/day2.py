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


#part 1
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

#part 2

power_sum = 0
for line in Lines:
    red = re.findall("(\d+) red", line)
    green = re.findall("(\d+) green", line)
    blue = re.findall("(\d+) blue", line)

    red = list(map(lambda a : int(a), red))
    green = list(map(lambda a : int(a), green))
    blue = list(map(lambda a : int(a), blue))
    
    red.sort()
    green.sort()
    blue.sort()
    power_sum += red[-1] * green[-1] * blue[-1]

print(power_sum)