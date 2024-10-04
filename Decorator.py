def my_decorator(func):
    # def wrapper():
        # Add behavior before calling the original function
        print("Something is happening before the function is called.")
        func()  # Call the original function
        # Add behavior after calling the original function
        print("Something is happening after the function is called.")
    # return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()