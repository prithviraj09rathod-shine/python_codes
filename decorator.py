def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print("Wrapper executed this before {}".format(original_function.__name__))
        y = 5
        z = 10
        x = y + z
        print("x :", x)
        square1 = x * x
        print("square of x:", square1)
        #original_function()
        return original_function(*args, **kwargs)
    wrapper_function()
    print("Wrapper executed just before returning the wrapper {}".format(original_function.__name__))  
    #b=5
    #c= 1
    a = 2
    print("a :", a)     
    cube1 = a * a * a
    print("cube of a:", cube1)
    return wrapper_function

@decorator_function
def display():
    print("Display function executed")  

display()