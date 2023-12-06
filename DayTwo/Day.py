ans = 0
try:
    # Open the file
    with open('input.txt', 'r') as file:
        # Read each line
        for line in file:
            tempLine = line.strip()
            gamePart = tempLine.split(":")
            setsPart = gamePart[1].split(";")
            possible = True
            colorDict = {"green":1, "blue":1, "red": 1}
            for s in setsPart:
                colors = s.split(",")
                for col in colors:
                    cube = col.strip().split(" ")
                    cubeAmount = int(cube[0])
                    cubeColor = cube[1]
                    """ -- PART ONE --
                    if((cubeColor == "red" and cubeAmount > 12) or
                       (cubeColor == "green" and cubeAmount > 13) or
                       (cubeColor == "blue" and cubeAmount > 14)):
                        possible = False
                        break                       
                if(not possible):
                    break
            if(possible):
                gameId = int(gamePart[0].strip().split(" ")[1])
                ans += gameId"""
                    tempColorAmount = colorDict[cubeColor]
                    if(tempColorAmount < cubeAmount):
                        colorDict[cubeColor] = cubeAmount
            multi = 1
            for tk in colorDict:
                tv = colorDict[tk]
                multi *= tv
            ans += multi # --- PART TWO ANSWER --- #
except FileNotFoundError:
    print("The file does not exist")
except IOError:
    print("The file could not be opened")
print(ans)