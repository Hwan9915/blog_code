class SimpleDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self):
        print("Something is happening before the function is called.")
        self.func()
        print("Something is happening after the function is called.")

@SimpleDecorator
def say_hello():
    print("Hello!")

say_hello()