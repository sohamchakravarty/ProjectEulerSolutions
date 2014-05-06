from time import time

def Fib(endValue):
    a,b = 1,2
    yield b
    while b<=endValue:
        a,b = b,a+b
        if b%2==0 : yield b
        endValue-=1

if __name__=='__main__':
    start = time()
    print sum(Fib(4000000))
    print time()-start
