import re
f=open("day 3\input.txt", "r")
board = f.read()

BOARD_LENGTH=re.search("^.*", board).span()[1]+1

#part 1

def check_bounding_box(match, board, string):
    number_span = match.span()
    box_span = [number_span[0]-1,number_span[1] + 1]
    if board[box_span[0]] == '\n':
        box_span[0] = number_span[0]
    
    top_line = [x for x in board[box_span[0]-BOARD_LENGTH:box_span[1]-BOARD_LENGTH] if box_span[0]-BOARD_LENGTH >= 0]
    mid_line = [x for x in board[box_span[0]:box_span[1]]]
    bot_line = [x for x in board[box_span[0]+BOARD_LENGTH:box_span[1]+BOARD_LENGTH] if box_span[0]+BOARD_LENGTH <= len(board)]
    
    bounding_box = "".join(top_line + mid_line + bot_line)

    if re.findall(string,bounding_box) == []:
        return False
    else:
        return True
   
allnums = [x for x in re.finditer("\d+", board)]
partnums = [match.group() for match in allnums if check_bounding_box(match, board, "[^\s.\d]")]
partnums = [int(x) for x in partnums]

print(sum(partnums))

#part 2

def check_gear_adjacency(match, board):
    gear_span = match.span()
    box_span = [gear_span[0]-1,gear_span[1] + 1]
    if board[box_span[0]] == '\n':
        box_span[0] = gear_span[0]
    
    top_line = "".join([x for x in board[box_span[0]-BOARD_LENGTH:box_span[1]-BOARD_LENGTH] if box_span[0]-BOARD_LENGTH >= 0])
    mid_line = "".join([x for x in board[box_span[0]:box_span[1]]]) 
    bot_line = "".join([x for x in board[box_span[0]+BOARD_LENGTH:box_span[1]+BOARD_LENGTH] if box_span[0]+BOARD_LENGTH <= len(board)])
    
    gear_adj_count = 0
    gear_adj_count += len(re.findall("\d+", mid_line))
    gear_adj_count += len(re.findall("\d+", top_line))
    gear_adj_count += len(re.findall("\d+", bot_line))

    if gear_adj_count == 2:
        return True
    else:
        return False
    
def gear_ratio_calc(gear, numbers):
    gearpoint = gear.span()[0]
    product = 1
    for number in numbers:
        number_span = number.span()
        box_span = [number_span[0]-1,number_span[1] + 1]
        if board[box_span[0]] == '\n':
            box_span[0] = number_span[0]

        if gearpoint in range(box_span[0], box_span[1]):
            product *= int(number.group())
        elif gearpoint in range(box_span[0]-BOARD_LENGTH, box_span[1]-BOARD_LENGTH) and box_span[0]-BOARD_LENGTH >= 0:
            product *= int(number.group())
        elif gearpoint in range(box_span[0]+BOARD_LENGTH, box_span[1]+BOARD_LENGTH) and box_span[0]+BOARD_LENGTH <= len(board):
            product *= int(number.group())

    return product

allgears = [x for x in re.finditer("\*", board)]
gears = [gear_ratio_calc(gear, allnums) for gear in allgears if check_gear_adjacency(gear,board)]

print(sum(gears))
    
