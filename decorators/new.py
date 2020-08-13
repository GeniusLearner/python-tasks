def add_one(number):
    return number + 1


add_one(2)

def sat_hello(name):
    return f'Hello {name}'

def greet_bob(greeter_func):
    return greeter_func("bob")


def parent(num):
    def first_child():
        return "Hi, I am Emma"

    def second_child():
        return "call me liam"

    if num == 1:
        return first_child
    else:
        return second_child



def my_decorator(func):
    def wrapper():
        print("Sonething is happening before the function is called")
        func()
        print("something is happening after the function is called.")
    return wrapper

def say_whee():
    print("Whee!")

say_whee = my_decorator(say_whee


from datetime impore datetime

def not_during_the_night(func):
    def wrapper():
        if 7 <= datetime.now().hour < 22:
            func()

        else:
            pass
        return wrapper

def say_whee():
    print("whee!")

say_whee = not_during_the_night(say_whee)


def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_whee():
    print("Whee!")
# @my_decorator means
# say_whee = my_decorator(say_whee)

