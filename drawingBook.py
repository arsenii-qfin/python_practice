def pageCount(n, p):
    
    frontCount = 0
    backCount = 0
    
    if p % 2 == 0:
        frontCount = int(p/2)
        if n % 2 == 0:
            backCount = int(n/2 - p/2)
        else:
            backCount = int((n-1)/2 - p/2)
    else:
        frontCount = int((p-1)/2)
        if n % 2 == 0:
            backCount = int(n/2 - (p-1)/2)
        else:
            backCount = int((n-1)/2 - (p-1)/2)
        
    finalCount = min(frontCount, backCount)
    
    return finalCount