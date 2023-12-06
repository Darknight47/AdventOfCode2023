ans = 0
try:
    # Open the file
    with open('input.txt', 'r') as file:
        # Read each line
        arr = []
        #-- SECOND PART --#
        
except FileNotFoundError:
    print("The file does not exist")
except IOError:
    print("The file could not be opened")
print(ans)

""" ------------ FIRST PART --------------
digitLst = re.findall('\d', tempLine)
    if(len(digitLst) == 1):
        tempStr = digitLst[0] + digitLst[0]
    else:
        tempStr= digitLst[0] + digitLst[len(digitLst) - 1]
        tempNum = int(tempStr)
        ans += tempNum
"""