#recursion code example in python
#1. factorial
#2. Fibonancii

def factorial(n):
    if n == 0: # Base case
        return 1
    else: # Recursive case
        return (n * factorial(n-1))
print(factorial(5))

#fibonacii
def fibonacii(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacii(n-1) + fibonacii(n-2)
print(fibonacii(10))