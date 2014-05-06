from math import sqrt
from time import time

#Factors of a number 'n' excluding 1 and n
def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n/i] for i in range(2, int(sqrt(n)) + 1) if n % i == 0)))

#Function to check if a number is prime
def isPrime(n):
     return all(n%i for i in xrange(2,int(sqrt(n))+1))

def LargestPrimeFactor(N):
    fctrs = sorted(factors(N))
    for fctr in fctrs[::-1]:
        if isPrime(fctr):
            return fctr
    
if __name__=="__main__":
    print(LargestPrimeFactor(600851475143))
