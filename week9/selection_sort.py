#Selection sort
data = [14,33,27,10,35,19,42,44]

# For loop - all the elements are going to be a starting point
for counter in range(len(data) - 1):
    min = counter

    # Look for a lower element in the rest of the list
    for internalCounter in range(counter+1, len(data)):
        if data[internalCounter] < data[min]:
            # Set the new minimum
            min = internalCounter

    # After the internal loop, swap the minimum element
    # With the current element
    if min!=counter:
        data[min], data[counter] = data[counter], data[min]

    print(data)     
