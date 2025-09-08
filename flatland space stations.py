#---Unoptimized Solution---#
def flatlandSpaceStations(n, c):
    globalMax = []
    for i in range(n): #iterate over all cities
        localMax = []
        for j in c: #find most distant space station
            d = abs(i-j)
            localMax.append(d)
        g = max(globalMax)
        globalMax.append(g)
    ans = max(globalMax)
    return ans

#---Optimized Solution---#
def flatlandSpaceStations(n, c):
    c.sort()
    left = c[0]-0
    right = (n-1)-c[-1]
    center = 0
    for i in range(len(c)-1):
        dist = (c[i+1]-c[i])//2
        center = max(center, dist)
        
    ans = max(left, right, center)
    return ans
