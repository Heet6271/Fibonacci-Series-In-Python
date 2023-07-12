def fib(n):
    a = 0
    b = 1
    
    if n == 1:
        print(a)
        
    elif n == 0:
        print('cannot generate')
        
    elif n == (-1):
        print('cannot generate')
        
    else:
        print(a)
        print(b)
        
    for i in range(2,n):
        c = a + b
        print(a+b)
        a = b
        b = c
        
x=int(input('enter the valu of n'))
fib(x)