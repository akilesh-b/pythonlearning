try:
    file = open("my", "r")

    content = file.read()

    words = content.split()

    count = len(words)

    print("Number of words in the file:", count)

    file.close()

except FileNotFoundError:
    print("File not found")