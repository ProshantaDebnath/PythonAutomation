file = open("textFile1.txt")
# read all the contents of the file
print(file.read())

# reading specific characters
print("reading specific characters : " + file.read(2))

# read one single line at a time readLind()
print(file.readline())
print(file.readline())

# Print line by line text file contents
line = file.readline()
while line != "":
    print(line)
    line = file.readline()

# Readiness is to store text data in list format by line by line
list = file.readlines()
for e in list:
    print(e)
# file.close()

