"""

# List

seq = [1,2,3,4,5]

for num in seq:
    print('Hello')

# String
mystring = 'Hello'

for char in mystring:
    print(char)

# Dictionary
salaries = {'John':10, 'Jenny':20, 'Shawn':30}

for employee in salaries:
    print(employee)

salaries = {'John':10, 'Jenny':20, 'Shawn':30}

for employee in salaries:
    print(salaries[employee])

salaries = {'John':10, 'Jenny':20, 'Shawn':30}

for employee in salaries:
    print(employee)
    print("has a salary of:")
    print(salaries[employee])
    print(' ')

i = 1
while i<5:
    print(f"i is currenty: {i}")
    i = i+1

# Functions

def report_person(name):
    print("reporting " + name)

report_person("Shawn")


def add_num(num1, num2):
    print(num1 + num2)

add_num(2,4)

def add_num(num1, num2):
    return num1 + num2

result = add_num(2,4)

print(result)
"""

