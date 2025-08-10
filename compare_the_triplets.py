def compareTriplets(a, b):
    result = [0, 0]
    for i, j in zip(a,b):
        if i == j:
            continue
        elif i>j:
            result[0] += 1
        else:
            result[1] += 1
    return result 
