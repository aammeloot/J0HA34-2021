# This is a bubble sort algorithm
#elements = [14, 23, 27, 35, 10]
elements = [23, 14, 27, 35, 10]

print("Starting:", elements)
# Let's create a flag to signal elements have been swapped
swapped = True  # By default it's true because you need to go through
                # the list at least once 

# Repeat until no swaps have occured
while swapped == True:
    # Flag up that no swaps have happened
    swapped = False

    # Loop through all the elements of the list
    # And swap them if they're not in increasing order
    # To avoid a crash we'll go from the first to
    # The penultimate element of the list

    # Get the length of the list as a reference
    length = len(elements)

    # Loop
    for counter in range(length - 1):
        # If the current element is greater than the next
        # swap them over
        a = elements[counter]
        b = elements[counter + 1]
        if a > b:
            # In another language you would do something like
            # c = a
            # a = b
            # b = c
            # Python method:
            a,b = b,a  # Magic! 
            # Save values back
            elements[counter] = a
            elements[counter +1] = b
            swapped = True
    
    print(elements)

print("Sorted:", elements)