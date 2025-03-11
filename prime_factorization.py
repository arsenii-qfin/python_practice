import time

a = int(float(input('Enter an Integer: ')))

while a <= 1:
    print('It has to be grater than 1')
    a = int(float(input('Enter an Integer:')))

'''
This is the logic to find the prime factors of a number.
It iterates by 1 starting from 2 and checks if the number is divisible by the iterator.
If the number is divisible by the iterator, the iterator is a prime factor and the number is diviede by it.
The iteration stops when the square root of the number becomes grater than the iterator. 
    -By the Division Theorem that states that any composite number n must have a prime divisor less than or equal to sqrt(n).
If the remaining factor is grater than 1, it is also a prime factor.
'''
def prime_factorization(a):
    prime_factors = []
    i = 2
    while i**2 <= a:
        while a % i == 0:
            prime_factors.append(i)
            a //= i
        i += 1
    if a > 1:
        prime_factors.append(a)

    return prime_factors

if __name__ == '__main__':
    factors = prime_factorization(a)
    print('Complex Computation in Progress...')
    time.sleep(2)
    print('Prime factorization of your number is: ', factors)

