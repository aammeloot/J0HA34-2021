# Binary search - data needs sorted already
data = [10,14,19,26,27,31,33,35,42,44]
print(data)

x = int(input("What are you searching for?"))
n = len(data)

lower = 0
upper = n - 1

found = False
position = -1

while not found:

    # if we have an upperboundary lower than the lower
    # boundary we exhausted the list and nothing was
    # found

    if lower > upper:
        print("Value not found")
        break 

    # Set a new "middle point"
    midPoint = int(lower + (upper - lower) / 2)
    print(midPoint)
    
    # If middle point is too small move lower
    if data[midPoint] < x:
        lower = midPoint + 1
    
    if data[midPoint] > x:
        upper = midPoint - 1

    if data[midPoint] == x:
        found = True
        print("Found at position", midPoint)

