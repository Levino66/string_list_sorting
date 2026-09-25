students = list()
user_input = input()
while user_input != 'stop':
    students.append(user_input)
    user_input = input()
    
students.sort()
for student in students:
    print(student)
