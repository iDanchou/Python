with open("test.txt", "r") as rf:  # rf for reading file
    with open("test_copy.txt", "w") as wf:  # wf for writing file
        for line in rf:
            wf.write(line)