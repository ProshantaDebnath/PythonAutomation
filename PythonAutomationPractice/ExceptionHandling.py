prdlist = {1, 5, 7, 8, 70}

for ele in prdlist:
    if ele == 70:
        raise Exception("Product is not good")
    else:
        print(ele)

for ele in prdlist:
    if ele == 5:
        assert False

# try, catch
try:
    with open('textFile1.txt', 'r') as file:
        for line in file:
            print(line)
        file.close()
except:
    print('File location is incorrect!')

# Exception printing
try:
    with open('textFile.txt', 'r') as file:
        file.readlines()
        file.close()
except Exception as e:
    print('File location is incorrect!')
    print(e)
finally:
    print('Cleaning up all the resources')