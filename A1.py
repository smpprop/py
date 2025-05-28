def find_unique(checklist):
    unique_list = []
    for item in checklist:
        if item not in unique_list:
            unique_list.append(item)

    return unique_list


def unique(ListA):
    unique = []
    for ele in listA:
        c = ListA.count(ele)
        if c == 1:
            unique.append(ele)
    return unique


N = int(input("Enter a N number of elements in the list: "))

listA = []
print(f"Enter any {N} elements: ")
for i in range(N):
    elements = input("Enter an elements: ")
    listA.append(elements)

list_unique = find_unique(listA)
print("The Unique elements are: ", list_unique)
unique_list = unique(listA)
print("The Unique",unique_list)
