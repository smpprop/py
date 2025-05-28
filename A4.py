input_str = input("Enter the Input string")
freq_all = {}
for x in input_str:
    if x in freq_all:
        freq_all[x]+= 1
    else:
        freq_all[x]=1
print(f"Frq of char:{str(freq_all)}")
