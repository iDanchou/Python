# WITHOUT LIST COMPREHENSION
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
new_list = []
for n in numbers:
    add_1 = n + 1

new_list.append(add_1)

# WITH LIST COMPREHENSION
# NEW_LIST = [NEW_ITEM FOR ITEM IN LIST]
new_list1 = [n + 1 for n in numbers]  # NUMBERS = [2, 3, 4]

name = "Sheen"
letters_list = [letter for letter in name]
# print(letters_list)

nums = range(1, 5)
nums_list = [n * 2 for n in nums]
print(nums_list)

# CONDITIONAL LIST COMPREHENSION
# NEW_LIST = [NEW_ITEM FOR ITEM IN LIST IF TEST]
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
print(short_names)

long_names = [name.upper() for name in names if len(name) > 5]  # WILL UPPERCASE ALL NAMES IN NEW LIST
print(long_names)

squared_nums = [n * n for n in numbers]
print(squared_nums)

even_nums = [n for n in numbers if (n % 2 == 0)]
print(even_nums)

with open("C:\/Users\/rkirk\Python\Python\Personal Projects\List Comprehension\/file1.txt") as file1:
    file_1_data = file1.readlines()

with open("C:\/Users\/rkirk\Python\Python\Personal Projects\List Comprehension\/file2.txt") as file2:
    file_2_data = file2.readlines()

result = [int(num) for num in file_1_data if num in file_2_data]
print(result)
