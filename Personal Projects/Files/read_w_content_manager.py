# Context manager
# Won't need to worry about closing file or cleanup

with open("test.txt", "r") as f:
    # prints entirety one line at a time
    """for line in f:'
        'print(line, end="")"""

    # Whole file, best for small files
    # Can optimize for size to print specified amount of data
    'size_to_read = 100'
    'f_contents = f.read(100)'  # Will print first 100 characters
    'print(f_contents, end="")'
    'f_contents = f.read(size_to_read)'  # Will print second 100 characters
    'print(f_contents, end="")'

    # Loops through contents 100 characters at a time
    """while len(f_contents) > 0:
        print(f_contents, end="")
        f_contents = f.read(size_to_read)
        print(f.tell())  # Will print current position in file
        f.seek(0)  # Sets position in file, will set at beginning
        """

    # List of all lines in file
    'f_contents = f.readlines()'
    'print(f_contents'

    # Prints one line, will need to run command multiple times to get entirety of file
    # Ends with newline at default
    'f_contents = f.readline()'
    'print(f_contents, end="")'
