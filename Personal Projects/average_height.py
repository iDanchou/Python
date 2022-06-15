student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])


total = 0
for x in student_heights:
    total += x

num_students = 0
for y in student_heights:
    num_students += 1


def average_function():
    average = total / num_students
    print(round(average))


average_function()
