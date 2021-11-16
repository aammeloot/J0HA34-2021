# Counting occurences
numbers = [10,44,12,23,43,10,22,10,44,22]

# User's search term
searchTerm = int(input("Please enter a number to search"))

# Counting the number of occurrences
counter = 0

for num in numbers:
    if num == searchTerm:
        counter+=1

print(searchTerm, "was found", counter, "times")