def migratoryBirds(arr):
    
    unique = {}
    
    for i in arr:
        if i in unique.keys():
            continue
        else:
            unique[i] = 1
    
    for i in unique.keys():
        n = arr.count(i)
        unique[i] = n
    
    maxVal = max(unique.values())
    
    maxIDs = [k for k,j in unique.items() if j == maxVal] #list compr
    
    ans = min(maxIDs)
    
    return ans