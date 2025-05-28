t1 = (1,2,5,7,97,24,6,8,10)
t2 = (11,13,15)

tp1 = t1[:5]
tp2 = t1[5:]

print("The first half of the tuple is:")
print(tp1)

print("The second half of the tuple")
print(tp2)

lst = list()
for x in t1:
    if x % 2 ==0:
        lst.append(x)

print("Tuple with even values")
tp3 = tuple(lst)
print(tp3)
print("Tuple Concatation")
t1=t1+t2
print(t1)

print("Maximum and minimum values")
print(max(t1))