def rotateLeft(d, arr):
    
    net = d % len(arr)
    rotated = [0]*len(arr)
    
    for i in range(len(arr)):
        n_idx = (i+net) % len(arr)
        rotated[i] = arr[n_idx]
    
    return rotated 