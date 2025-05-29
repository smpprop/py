t1 = (1,2,5,7,97,24,6,8,10)
t2 = (11,13,15)

print("First half:\n",t1[:5])
print("First second:\n",t1[5:])

lst = list()
for x in t1:
    if x % 2 == 0:
        lst.append(x)
print("Tupple with even values:\n",tuple(lst))
t1 = t1+t2
print("Tuple Concatination:\n",t1)
print("Tuple max:\n",max(t1))
print("Tuple min:\n",min(t1))
