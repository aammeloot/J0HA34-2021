# Empty array
students = []

name = input("Enter the name of a student")

while name != "stop":
    students.append(name)
    name = input("Enter the name of a student")

print("You have", len(students), "students.")

print(students)
students.sort()  # Sorting alphabetically
print(students)

if "Michael" in students:
    print("I'm sure Michael is in another group now")

