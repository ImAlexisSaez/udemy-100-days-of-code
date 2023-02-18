import time


def delay_decorator(function):
    def wrapper_function():
        # Do something before the function
        time.sleep(2)
        function()
        # function()  # Modify the function running it two times.
        # Do something after the function

    return wrapper_function


@delay_decorator
def say_hello():
    print("Hello")


@delay_decorator
def say_bye():
    print("Bye")


@delay_decorator
def say_greeting():
    print("How are you?")


say_hello()
say_bye()
say_greeting()

# Calling decorators without syntactic sugar
decorated_function = delay_decorator(say_bye)
decorated_function()