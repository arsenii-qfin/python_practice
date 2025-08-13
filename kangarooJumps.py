def kangaroo(x1, v1, x2, v2):
    
    if v1 == v2:
        return "YES" if x1 == x2 else "NO"
        
    if (x1 < x2 and v1 <= v2) or (x1 > x2 and v1 >= v2):
        return "NO"
    
    n = (x1 - x2) / (-v1 + v2) #must satisfy
    
    return "YES" if n >= 0 and n % 1 == 0 else "NO"