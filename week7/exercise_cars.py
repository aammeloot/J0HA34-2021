
# Create a new empty Python dictionary called cars
cars = {}

# Manually in your code, add a couple of entries to the dictionary.
# The Key should be the name of the person, the Value their car registration. 
cars['Chloe Gad'] = 'CL03 GAD'
cars['Napoleon Dynamite'] = 'T1N4 34T'
cars['Casey Donaldson'] = 'CA53 DON'
cars['Christian Swankie'] = 'SW04 NKY'
cars['Joe Swindells'] = 'SW15 DEL'
cars['John Doe'] = 'J003 D00'

# Using a for loop, write code to get the user to add a some more entries to the dictionary. 
# Remember you will need to collect TWO bits of data from user (name and reg number) for each dictionary entry
''' for counter in range(2):
    name = input('Enter the name of the car owner')
    reg = input('Enter their registration number')
    # Add to the dictionary
    cars[name] = reg '''

# Print out the whole dictionary
print(cars)

# Print out the size of the car registration dictionary
print(len(cars))

# Remove one of the entries from the dictionary
# Print out the size of the dictionary to verify that the Step 6 worked
cars.pop('Chloe Gad')
print(len(cars))

# Print out the whole dictionary again, but this time by iterating through it on pair at a time.
# Each line should look similar to: 
# “John Smith’s car is registration XXXXXX”
for name, reg in cars.items():
    print(name + '\'s car registration is ' + reg)

# Find out if the name “Cornelius Snape” is in the list, and print out the answer 
# (i.e. “Cornelius Snape’s reg number is XXXXX” or “Cornelius Snape is not in the list”)
# If “Cornelius Snape” is not in your dictionary, add him and test again. 
# Always make sure to test BOTH outcomes of an IF

if 'Cornelius Snape' in cars:
    print('Cornelius Snapes\' car registration is' + cars['Cornelius Snape'])
else:
    print('We don\'t have Cornelius Snapes\' car registration')

# Find all names in the list which begin with the letter J,
# and for each change the value of their pair to “BANNED”.
# (If you don’t have any names beginning with J in your list,
# search for a letter you do have, or add some names beginning with J!)

# Ban all users in J
for name in cars.keys():
    #if name.startswith('J'):
    if name[0] == 'J':
        cars[name] = 'BANNED'

# Print out a nicely formatted list of employees 
# who are banned from the car park (i.e. employees whose Value is “BANNED”)

# List all banned users
print('List of banned users:')
for name, reg in cars.items():
    if reg == 'BANNED':
        print(name)

