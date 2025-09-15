#lambda function: inline evaluation/operation/, used when single iteration is needed
x = lambda a : a + 10
print(x(5)) 

def func(n):
    return lambda a : a * n

doubler = func(2)
tripler = func(3)
print(doubler(11))  #22
print(tripler(11))  #33
