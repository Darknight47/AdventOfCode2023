ans = 0
try:
    # Open the file
    with open('input.txt', 'r') as file:
        # Read each line
        for line in file:
            # Print the line
            tempLine = line.strip().split(":")
            nums = tempLine[1].strip().split("|")
            winningNums = set(map(int, nums[0].strip().split()))
            otherNums = list(map(int, nums[1].strip().split()))
            commonNums = len(winningNums.intersection(otherNums))
            power = commonNums - 1
            tempAns = 0
            if(power < 0):
                tempAns = 0
            else:
                tempAns = 2 ** power
            ans += tempAns
except FileNotFoundError:
    print("The file does not exist")
except IOError:
    print("The file could not be opened")
print(ans)