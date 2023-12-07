from collections import Counter
fiveOfKind = {}
fourOfKind = {}
fullHouse = {}
threeOfKind = {}
twoPair = {}
onePair = {}
highCard = {}
try:
    # Open the file
    with open('DaySeven/input.txt', 'r') as file:
        # Read each line
        for line in file:
            tempLine = line.strip().split(" ")
            tempKey = tempLine[0]
            tempValue = tempLine[1]
            tempSet = set(tempKey)
            if(len(tempSet) == 5): #High_Card
                highCard[tempKey] = int(tempValue)
            elif(len(tempSet) == 1): # Five_Of_Kind
                fiveOfKind[tempKey] = int(tempValue)
            elif(len(tempSet) == 2): 
                freq = Counter(tempKey)
                freq_counts = Counter(freq.values())
                if freq_counts == {4:1, 1:1}: # Four_Of_Kind
                    fourOfKind[tempKey] = int(tempValue)
                elif(freq_counts == {2:1, 3:1}): # Full_House
                    fullHouse[tempKey] = int(tempValue)
            elif(len(tempSet) == 3):
                freq = Counter(tempKey)
                freq_counts = Counter(freq.values())
                if(freq_counts == {3:1, 1:2}): # Three_Of_Kind
                    threeOfKind[tempKey] = int(tempValue)
                elif(freq_counts == {2:2, 1:1}): # Two_Pair
                    twoPair[tempKey] = int(tempValue)
            elif(len(tempSet) == 4):
                onePair[tempKey] = int(tempValue)
except FileNotFoundError:
    print("The file does not exist")
except IOError:
    print("The file could not be opened")
# Custom order
order = "23456789TJQKA"
# Create a mapping of character to its strength based on the order
strength_map = {char: index for index, char in enumerate(order)}
# Custom key function for sorting
def sort_key(s):
    # Map the string to a tuple of its characters' strengths
    return tuple(strength_map[char] for char in s)

# Sort the dictionary keys based on the custom order
fiveOfKind_sortedKeys = sorted(fiveOfKind.keys(), key=sort_key, reverse=False)
# Create a new dictionary with sorted keys
fiveOfKind_sorted = {key: fiveOfKind[key] for key in fiveOfKind_sortedKeys}

fourOfKind_sortedKeys = sorted(fourOfKind.keys(), key=sort_key, reverse=False)
fourOfKind_sorted = {key: fourOfKind[key] for key in fourOfKind_sortedKeys}

fullHouse_sortedKeys = sorted(fullHouse.keys(), key=sort_key, reverse=False)
fullHouse_sorted = {key: fullHouse[key] for key in fullHouse_sortedKeys}

threeOfKind_sortedKeys = sorted(threeOfKind.keys(), key=sort_key, reverse=False)
threeOfKind_sorted = {key: threeOfKind[key] for key in threeOfKind_sortedKeys}

twoPair_sortedKeys = sorted(twoPair.keys(), key=sort_key, reverse=False)
twoPair_sorted = {key: twoPair[key] for key in twoPair_sortedKeys}

onePair_sortedKeys = sorted(onePair.keys(), key=sort_key, reverse=False)
onePair_sorted = {key: onePair[key] for key in onePair_sortedKeys}

highCard_sortedKeys = sorted(highCard.keys(), key=sort_key, reverse=False)
highCard_sorted = {key: highCard[key] for key in highCard_sortedKeys}

coefficient = 1
highCard_result = 0
for i in highCard_sorted:
    tv = highCard_sorted[i]
    highCard_result += coefficient * tv
    coefficient += 1
onePair_result = 0
for i in onePair_sorted:
    tv = onePair_sorted[i]
    onePair_result += coefficient * tv
    coefficient += 1
twoPair_result = 0
for i in twoPair_sorted:
    tv = twoPair_sorted[i]
    twoPair_result += coefficient * tv
    coefficient += 1
threeOfKind_result = 0
for i in threeOfKind_sorted:
    tv = threeOfKind_sorted[i]
    threeOfKind_result += coefficient * tv
    coefficient += 1
fullHouse_result = 0
for i in fullHouse_sorted:
    tv = fullHouse_sorted[i]
    fullHouse_result += coefficient * tv
    coefficient += 1
fourOfKind_result = 0
for i in fourOfKind_sorted:
    tv = fourOfKind_sorted[i]
    fourOfKind_result += coefficient * tv
    coefficient += 1
fiveOfKind_result = 0
for i in fiveOfKind_sorted:
    tv = fiveOfKind_sorted[i]
    fiveOfKind_result += coefficient * tv
    coefficient += 1
ans = highCard_result + onePair_result + twoPair_result + threeOfKind_result + fullHouse_result + fourOfKind_result + fiveOfKind_result
print("Answer For the first part: ", ans)