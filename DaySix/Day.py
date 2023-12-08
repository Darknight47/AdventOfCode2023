time = [48, 93, 84, 66] # ---- INPUT 
distance = [261, 1192, 1019, 1063] # ---- INPUT
firstPartAns = 1
for i in range(4):
    t = time[i]
    dist = distance[i]
    tempAns = 0
    for j in range(1, t):
        temp = t - j
        tempDist = j * temp
        if(tempDist > dist):
            tempAns += 1
    firstPartAns *= tempAns
print(firstPartAns) # -------- FIRST PART ---------- #

# Race parameters
T = 48938466  # Total time of the race in milliseconds
record_distance = 261119210191063  # Record distance in millimeters

# Function to calculate the distance traveled by the boat
def distance_traveled(t, T):
    return t * (T - t)

# Initialize pointers
lower_bound = 1
upper_bound = T - 1

# Find the first number greater than the record distance
while lower_bound < T:
    if distance_traveled(lower_bound, T) > record_distance:
        break
    lower_bound += 1

# Find the last number greater than the record distance
while upper_bound > 0:
    if distance_traveled(upper_bound, T) > record_distance:
        break
    upper_bound -= 1

# Calculate the number of ways to beat the record
ways_to_beat_record = upper_bound - lower_bound + 1 # -------- SECOND PART --------- #

# Output the result
print(f"You could hold the button anywhere from {lower_bound} to {upper_bound} milliseconds and beat the record, a total of {ways_to_beat_record} ways!")