from decorators import do_twice

@do_twice
def greet(name):
    print(f"Hello {name}")


    # >>>greet("world")
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: wrapper_do_twice() takes 0 positional arguments but 1 was given


