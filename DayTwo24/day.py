ans = 0
try:
    # Open the file
    with open('DayTwo24/input.txt', 'r') as file:
        # Read each line
        for line in file:
            dec = False
            inc = False
            ok = True
            arr = [int(num) for num in line.split()]
            for j in range(len(arr) - 1):
                first = arr[j]
                second = arr[j + 1]
                if(second > first):
                    inc = True
                elif(second < first):
                    dec = True
                else:
                    ok = False
                    break
                if(inc and dec):
                    ok = False
                    break
                diff = abs(second - first)
                if(diff < 1 or diff > 3):
                    ok = False
                    break
            if(ok):
                ans += 1
except FileNotFoundError:
    print("The file does not exist")
except IOError:
    print("The file could not be opened")
print(ans)
