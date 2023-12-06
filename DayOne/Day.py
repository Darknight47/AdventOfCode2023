import re
ans = 0
number_words = {
    'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
    'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
}

try:
    # Open the file
    with open('input.txt', 'r') as file:
        # Read each line
        arr = []
        # Create a regex pattern to match string numbers or single digits
             
        for line in file:
            # Print the line
            tempLine = line.strip()
            pattern = r'\b(?:' + '|'.join(number_words.keys()) + r')\b|\d'  
            # Find all matches in the input string
            matches = re.findall(pattern, tempLine)
            # Replace string numbers with their corresponding digits
            separated_numbers = [number_words.get(match, match) for match in matches]
            print("2")
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