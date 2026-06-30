# ----------------------------------------------------
# Activity 2 : Type Casting
# ----------------------------------------------------

# Creating Variables
name = "Penguin"
age = 15
is_student = True
weight = 38.5

# Printing Variables and their Data Types
print("Name :", name)
print("Data Type :", type(name))

print()

print("Age :", age)
print("Data Type :", type(age))

print()

print("Student :", is_student)
print("Data Type :", type(is_student))

print()

print("Weight :", weight)
print("Data Type :", type(weight))

print("\n------ After Type Casting ------")

# Integer to String
age = str(age)

print("Age :", age)
print("Data Type :", type(age))

print()

# Float to Integer
weight = int(weight)

print("Weight :", weight)
print("Data Type :", type(weight))
