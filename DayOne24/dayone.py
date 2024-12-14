from collections import Counter

ans = 0
leftArr = []
rightArr = []
try:
    # Open the file
    with open('DayOne24/input.txt', 'r') as file:
        # Read each line
        for line in file:
            # Print the line
            tempLine = line.strip().split("   ")
            leftNum = int(tempLine[0])
            rightNum = int(tempLine[1])
            leftArr.append(leftNum)
            rightArr.append(rightNum)
except FileNotFoundError:
    print("The file does not exist")
except IOError:
    print("The file could not be opened")
# ------ PART ONE -------
# leftArr = sorted(leftArr)
# rightArr = sorted(rightArr)
# for j in range(len(leftArr)):
#     ans += abs(leftArr[j] - rightArr[j])
# print(ans) 

# ------ PART TWO -------
leftCounter = Counter(leftArr)
rightCounter = Counter(rightArr)
tempSet = set()
for num in leftArr:
    if num not in tempSet:
        leftCount = leftCounter[num]
        rightCount = rightCounter[num]
        temp = num * leftCount
        temp *= rightCount
        ans += temp
        tempSet.add(num)
print(ans)