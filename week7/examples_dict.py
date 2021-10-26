fruit = {}

fruit[1] = 'apple'
fruit[2] = 'pear'

print(fruit)

person = {}

person['name'] = 'Jack'
person['age'] = 27

print(person)

phonebook = { 'John Smith' : '01234 567543', 'Jane Jones':'01725 456838' }

print(phonebook['John Smith'])
phonebook['Craig Simpson'] = '01726 574635'

print(phonebook)
phonebook['Craig Simpson'] = '01726 758349'
print(phonebook)

# This is going to display all the content of the dictionary
# Key / Value side by side
for key, value in phonebook.items():
    print(key, value)

for key in phonebook.keys():
    print(key)