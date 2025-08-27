def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print("Wrapper executed this before {}".format(original_function.__name__))
        y = 5
        z = 10
        x = y + z
        print("x :", x)
        square1 = x * x
        print("square of x:", square1)
        original_function()
        return original_function(*args, **kwargs)
        print("Wrapper executed this after {}".format(original_function.__name__))  
    return wrapper_function

@decorator_function
def display():
    print("Display function executed")  

display()