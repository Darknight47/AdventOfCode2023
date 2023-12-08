instructions = ""
network = {}
try:
    # Open the file
    with open('DayEight/input.txt', 'r') as file:
        instructions = file.readline().strip()
        file.readline()
        # Read each line
        for line in file:
            # Print the line
            tempLine = line.strip().split("=")
            tk = tempLine[0].strip()
            tv = tempLine[1].strip()
            network[tk] = tv
except FileNotFoundError:
    print("The file does not exist")
except IOError:
    print("The file could not be opened")
founded = False
indx = 0
movement = network["AAA"]
ans = 0
while not founded:
    tempAction = instructions[indx]
    movementLst = movement.strip().replace("(", "").replace(")", "").replace(" ", "").split(",")
    indx += 1
    ans += 1
    if(indx >= len(instructions)):
        indx = 0
    if(tempAction == "L"):
        tempMove = movementLst[0]
    else:
        tempMove = movementLst[1]
    if(tempMove == "ZZZ"):
        founded = True
        break
    movement = network[tempMove]
print("First Part Answer: ", ans)