# List of elements
names = ['John', 'Jack', 'Emily', 'Chloe']

for n in names:
    print(n)

# The code above is a "for each" loop
# Where the variable n collects the "current"
# Element in the list

# In Python there's no traditional "for loop" with a counter
# But you can use the same syntax on a range and get 
# A similar result

for counter in range(10):
    print(counter)

# If you need the index in a list, you can do that
# This is more like a traditional way to access
# Values in a list/array like you'd do in 
# C/C++/Visual Basic etc.
for position in range(len(names)):
    print(position, names[position])

# BREAKING NEWS
# Strings work the same way
for letter in 'Aurelien':
    print(letter)

name = 'Aurelien'
print(name[:3])