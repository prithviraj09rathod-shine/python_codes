""" def gen_fun(x):
    #y = x * 2
    yield x
    yield x + 1
    yield x + 2
x = 10
gen_obj = gen_fun(x)
#print(list(gen_obj))  #converts generator to list
print(next(gen_obj))
print(next(gen_obj))
print(next(gen_obj)) """

list1 = (x*x for x in range(1,11))
print(list1)
print(next(list1))
print(next(list1))
print(next(list1))