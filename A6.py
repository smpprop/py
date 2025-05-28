words = 0
line = 0
chars = 0

f = open("Example.txt", "w")
f.write("Today is Monday \n Tomorrow is Tuesday \n Thankyou")
f.close()

with open("Example.txt", 'r') as fp:
    line = len(fp.readlines())
print('Total Number of Lines : ', line)

with open("Example.txt", 'r') as fp:
    for line in fp:
        temp = line.split()
        words += len(temp)
print("Number of words:", words)

with open("Example.txt", 'r') as fp:
    data = fp.read()
    chars = len(data)
print("Number of characters:", chars)
