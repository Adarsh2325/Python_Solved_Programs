def factorial(n,fact=1):
    for val in range(1,n+1):
        fact=fact*val
    return fact
n=5
print(factorial(n))
