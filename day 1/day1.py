import re
f=open("input.txt", "r")
Lines = f.readlines()

def digit_search(str, dir):
    words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    digitpos = list()
    if dir == "reverse":
        digitpos = [[str.rfind(x),int(x)] for x in str if x.isdigit()]
        digitpos += [[str.rfind(x),words.index(x)] for x in words if x in str]
        digitpos.sort(reverse=True)
    else:
        digitpos = [[str.find(x),int(x)] for x in str if x.isdigit()]
        digitpos += [[str.find(x),words.index(x)] for x in words if x in str]
        digitpos.sort()
    return digitpos[0][1]

#part 1
digitslist = []
for line in Lines:
    digitslist.append((int([x for x in line if x.isdigit()][0]) * 10) + int([x for x in line if x.isdigit()][-1]))
print(sum(digitslist))

#part 2
digitslist = []
for line in Lines:
    digitslist.append((digit_search(line, "forward") * 10) + digit_search(line, "reverse"))
print(sum(digitslist))

