char = word = line_count = 0

with open('text.txt','w') as fp:
    fp.write("Text Content \n New Contents")
with open('text.txt','r')as fp:
    for line in fp:     
        line_count += 1
        word += len(line.split())
        char += len(line)

print(f"Num of char:{char}")
print(f"Num of word:{word}")
print(f"Num of lines:{line_count}")
