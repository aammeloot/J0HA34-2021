# Linear search
sorted = [10,14,19,26,27,31,33,35,42,44]
unsorted = [10,35,26,14,33,42,44,19,31,27]

#data = sorted
data = unsorted

n = int(input("What number are you searching for?"))
position = -1 # That's the position of the element not found yet
for counter in range(len(data)):
    if data[counter] == n:
        position = counter
        break

if position != -1:
    print("The element you look for is in position", position)
else:
    print("Element not found")

