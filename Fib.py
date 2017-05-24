prevfib = 1
fib = 0

n = 100000

arr = [fib]

for i in range(n):
    fib = fib + prevfib
    prevfib = fib - prevfib
    if fib == 99194853094755497:
        print(i + 1)
    #arr.append(fib)

#print(fib)