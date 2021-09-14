# Find the maximum among two numbers

# Display “Enter a first number”
# Create variable number1 and read input to it
# Display “Enter a first number”
# Create variable number2 and read input to it

number1 = int(input('Enter a first number'))
number2 = int(input('Enter a second number'))

# If first number1 >= number2 then
#     Display number1
# Else
#     Display number2
# End if

if number1 >= number2:
    print(number1, 'is the largest')
else:
    print(number2, 'is the largest')
