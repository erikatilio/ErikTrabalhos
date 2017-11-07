def fib2(n):
    a = 0
    b = 1
    print(a)
    while b < n:
        c = a
        a = b
        b = a + c
        print(a)
fib2(8)