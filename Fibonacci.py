def fib():
    n1=0
    n2=1
    print(0,n1)
    print(1,n2)
    for i in range(2,100):
        n=n1+n2
        print(i,n)
        n1=n2
        n2=n

if __name__ == '__main__':
    fib()