student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

highest_value = 0
for x in student_scores:
    if x > highest_value:
        highest_value = x

print(f"The highest score in the class is:{highest_value}")
