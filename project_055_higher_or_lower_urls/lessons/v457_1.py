# Create the logging_decorator() function 👇
def logging_decorator(function):
    def wrapper(*args, **kwargs):
        print(f"You called {function.__name__}{args}")
        result = function(args)
        print(f"It returned: {result}")
    return wrapper


# Use the decorator
@logging_decorator
def sum_list(a_list):
    return sum(a_list)


sum_list(1, 2, 3, 4)