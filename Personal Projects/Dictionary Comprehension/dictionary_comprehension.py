# NEW_DICT = {NEW_KEY:NEW_VALUE FOR ITEM IN LIST} TO CREATE A DICTIONARY FROM A LIST OR DICTIONARY
# NEW_DICT = {NEW_KEY:NEW_VALUE FOR (KEY, VALUE) IN DICT.ITEMS()} CREATE A DICTIONARY FROM A DICTIONARY
# NEW_DICT = {NEW_KEY:NEW_VALUE FOR (KEY, VALUE) IN DICT.ITEMS() IF TEST}
import random
import pandas

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

student_scores = {student: random.randint(1, 100) for student in names}
print(student_scores)

passed_students = {student: score for (student, score) in dict.items(student_scores) if score > 60}
print(passed_students)

# CREATE A DICTIONARY THAT LISTS NUMBER OF LETTERS IN EACH WORD
sentence = "What is the airspeed velocity of an Unladen Swallow?"
word_list = sentence.split()
# print(word_list)
result = {words: len(words) for words in word_list}
print(result)

#  CONVERT DICTIONARY OF TEMPS IN CELSIUS TO FAHRENHEIT
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24
}

weather_f = {day: (temp * 9/5) + 32 for (day, temp) in dict.items(weather_c)}
print(weather_f)


student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

student_df = pandas.DataFrame(student_dict)
# LOOP THROUGH ROWS RATHER THAN COLUMNS
for (index, row) in student_df.iterrows():
    print(row)
