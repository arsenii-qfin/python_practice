def nonDivisibleSubset(k,s):
    counts = [0]*k
    ans = 0

    for i in s:
        r = i % k
        counts[r] +=1

    if k % 2 == 0:
        if counts[k//2] > 0:
            ans += 1
    
    if counts[0] > 0:
        ans += 1

    for r in range(1, (k+1)//2):
        if r == k-r:
            continue
        add = max(counts[r], counts[k-r])
        ans += add
    
    return ans