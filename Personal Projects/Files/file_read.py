# Opens the file
# to read = r, to write = w, to append = a, to read and write = r+
f = open("test.txt", "r")

print(f.name)
print(f.mode)

# Closes file, MUST close file
f.close()
