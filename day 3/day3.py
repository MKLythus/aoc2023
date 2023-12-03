import re
f=open("day 3\input.txt", "r")
board = f.read()

BOARD_LENGTH=141

#part 1

def check_bounding_box(match, board):
    number_span = match.span()
    box_span = [number_span[0]-1,number_span[1] + 1]
    if board[box_span[0]] == '\n':
        box_span[0] = number_span[0]
    
    top_line = [x for x in board[box_span[0]-BOARD_LENGTH:box_span[1]-BOARD_LENGTH] if box_span[0]-BOARD_LENGTH >= 0]
    mid_line = [x for x in board[box_span[0]:box_span[1]]]
    bot_line = [x for x in board[box_span[0]+BOARD_LENGTH:box_span[1]+BOARD_LENGTH] if box_span[0]+BOARD_LENGTH <= len(board)]
    
    bounding_box = "".join(top_line + mid_line + bot_line)

    if re.findall("[^\s.\d]",bounding_box) == []:
        return False
    else:
        return True
   
allnums = [x for x in re.finditer("\d+", board)]
partnums = [match.group() for match in allnums if check_bounding_box(match,board)]
partnums = [int(x) for x in partnums]

print(sum(partnums))