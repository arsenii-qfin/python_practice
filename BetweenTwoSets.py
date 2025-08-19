def getTotalX(a, b):
    
    minB = min(b)
    comDivisorsB = []
    final = []
    
    for i in range(1, minB+1):
        checkpoint = True
        for j in b:
            if j % i == 0:
                continue
            else: 
                checkpoint = False
                
        if checkpoint:
            comDivisorsB.append(i)
    
    if comDivisorsB == []:
        return 0
    
    for i in comDivisorsB:
        checkpoint = True
        for j in a:
            if i % j == 0:
                continue
            else:
                checkpoint = False
        
        if checkpoint:
            final.append(i)
    
    return len(final)