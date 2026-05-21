file = open("rathina.txt", "r")

content = file.read()

words = content.split()

count = len(words)

print("Total words:", count)

file.close()