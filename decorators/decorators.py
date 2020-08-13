def do_twice(func):
    def wrapper_do_twice():
        func()
        func()
    return wrapper_do_twice


# for adding positional arguments

def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper_do_twice

    #>>> greet("World")
# Hello World
# Hello World


def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_do_twice


>> > return_greeting("Adam")
Creating greeting
Creating greeting
'Hi Adam'


#For maintaining the information of the original function

imort functools

def do_twice(func):
    @functools.wraps(func)
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_do_twice


import functools

def decorator(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        # do something befor
        value = func(**args, **kwargs)
        # do something after
        return value
    return wrapper_decorator



from flask import Flask, g, request, redirect, url_for
import functools
app = Flask(__name__)

def login_required(func)
