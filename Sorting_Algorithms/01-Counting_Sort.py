# non-negative integer list to be sorted
# inputArray = [2, 5, 3, 0, 2] original one 
inputArray = [2, 5, 6, 3, 4, 5, 6, 6, 2, 0]

# Step 1
maxElement = max(inputArray)


# Step 2
countArray = [0] * (maxElement + 1)


# Step 3
for integer in range(maxElement + 1):
    countArray[integer] = len([i for i in inputArray if i == integer])


# Step 4
# cumulative countArray
for i in range(1, len(countArray)):
    countArray[i] += countArray[i - 1]
    
    
    
# Step 5
outputArray = [0] * len(inputArray)


# Step 6
for integer in inputArray[::-1]:
    outputArray[countArray[integer] - 1] = integer
    countArray[integer] -= 1