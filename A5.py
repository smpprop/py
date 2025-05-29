def nearly_equal(a, b):
    if(len(a) != len(b)):       
        return False
    count = 0
    for i in range(len(a)):    
        if a[i] != b[i]:
            count += 1
        if count > 1:             
            return False
    return count == 1             
