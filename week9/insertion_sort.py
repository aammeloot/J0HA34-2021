# Insertion sort
elements = [14, 33, 27, 10, 35, 19, 42, 44]
print("Start:", elements)

# By default we consider the first element
# Sorted
for counter in range(1, len(elements)):
    # Current value is value to insert
    valueToInsert = elements[counter]
    holePosition = counter

    # Locate hole position
    while holePosition > 0 and elements[holePosition -1] > valueToInsert:
        elements[holePosition] = elements[holePosition - 1]
        holePosition = holePosition -1

        #print(elements)
    
    elements[holePosition] = valueToInsert
    print(elements)