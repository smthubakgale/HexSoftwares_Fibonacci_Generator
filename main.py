def fibo(num):
    if num <= 1:
        return 1
    return fibo(num - 1) + fibo(num - 2)

def fibonacci(num):
    arr = []
    for i in range(num):
        arr.append(fibo(i))
    return arr

seq = fibonacci(6)

print(seq)

