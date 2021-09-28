students = ('Casey', 'Paul', 'Chloe', 'Michael')

# This is a tuple, aka a list that cannot be changed

print(students)
print(students[:2])

for name in students: # Modern for loop (no counter)
    print(name)         # Aka a "for each" loop

changeable = list(students) # If you need a mutable list, you need to cast