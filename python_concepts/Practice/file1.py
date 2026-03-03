def generator_fun(y):
    yield y+1
    yield y+2
    yield y+3
gen = generator_fun(5)
print(next(gen))
print(next(gen))
print(next(gen))