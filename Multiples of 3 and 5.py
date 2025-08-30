
#--returns the sum of all multiples of 3 and 5 below n---#

def foo(n):

    mult = []
    n1=3
    m1=1

    while m1*n1 < n:
        k = m1*n1
        mult.append(k)
        m1 +=1

    n2=5
    m2=1

    while m2*n2 < n:
        k = m2*n2
        mult.append(k)
        m2 +=1

    return print(sum(mult))

n=10
foo(n)