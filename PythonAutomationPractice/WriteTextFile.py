# read the file and store all the line in list
# reverse the list
# write the list bact to the file

with open('textFile1.txt','r') as reader:
    content = reader.readlines()

    with open('textFile1.txt', 'w') as writer:
        for line in reversed(content):
            writer.write(line)


    
