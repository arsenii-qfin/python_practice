import random as rd

def split(list:list):
    """
    Divite a passed in list into two
    """
    midpoint = len(list)//2
    left = list[:midpoint]
    right = list[midpoint:]

    return left, right

def merge(left:list, right:list):
    """
    Sorts and merges two passed in lists
    """
    l = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1
    #finish off remainings of left list if any
    while i < len(left):
        l.append(left[i])
        i += 1
    #finiah off remainings of right list if any
    while j < len(right):
        l.append(right[j])
        j += 1
    
    return l



def merge_sort(list:list):
    """
    Sorts a list in ascending order.
    """
    if len(list) <= 1:
        return list
    
    left, right = split(list)
    #called until <= 1 stopping conditin is reached
    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def random_list(n:int):
    out = []
    for i in range(n):
        r = rd.randint(0,2000)
        out.append(r)

    return out

def verify(sorted:list):
    n = len(sorted)

    if n <=1:
        return True
    
    return sorted[0] <= sorted[1] and verify(sorted[1:])

alist = random_list(500)
print(alist, " \n")

out = merge_sort(alist)

print(out)

print(verify(out))