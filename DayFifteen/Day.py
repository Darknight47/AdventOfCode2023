sequences = []
try:
    # Open the file
    with open('DayFifteen/input.txt', 'r') as file:
        for line in file:
            # Print the line
            sequences = line.strip().split(",")
            #sequences.append(tempLine)
except FileNotFoundError:
    print("The file does not exist")
except IOError:
    print("The file could not be opened")
ans = 0
for seq in sequences:
    value = 0
    for ch in seq:
        tempAscii = ord(ch)
        value += tempAscii
        tempValue = value * 17
        value = (tempValue % 256)
    #print("Value Temp: ", value)
    ans += value
print(ans)