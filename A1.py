list1 = []
unique_list =[]
n = int(input("Enter the number of list:"))
for i in range(n):
    item = int(input("Enter list in item:"))
    list1.append(item)
for x in list1:
    if list1.count(x) ==1:
        unique_list.append(x)
print(unique_list)
