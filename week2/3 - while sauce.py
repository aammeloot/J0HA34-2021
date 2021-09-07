# Construct 3: while loop
# Controlled with a condition

# 'forcing' the condition into the variable
# This is a variable
tomatoes_left = 'yes'

print('Putting pan on low heat')
print('Pan is hot')

# Here comes the loop below

# While the variable is a of specific value
# Run the code below
while tomatoes_left == 'yes':
    print('Chopping tomato')
    print('Adding to pan')
    # in order to avoid an infinite loop, make
    # sure to have an input in the loop  
    tomatoes_left = input('Any tomatoes left?')

print('Adding spices')
print('Cooking 20 minutes')
print('Add to pasta!')
