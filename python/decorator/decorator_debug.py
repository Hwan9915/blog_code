def debug(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"{func.__name__} called with {args}, {kwargs} returned {result}")
        return result
    return wrapper

@debug
def make_greeting(name, age=None):
    greeting = f"Hello {name}"
    if age:
        greeting += f", you are {age} years old!"
    return greeting

make_greeting("Alice", age=30)
