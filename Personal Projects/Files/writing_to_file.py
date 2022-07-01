# Will create file if it does not exist
with open("test3.txt", "w") as f:
    f.write("Test")
    # Second command will overwrite whatever is at the 0th position only
    f.seek(0)
    f.write("R")
