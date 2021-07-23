
import os


def cls(): return os.system('clear')


def bind_event(target, event, method):
    if type(target) == str and type(event) == str and type(method) == function:
        target.bind("<{}>".format(event), method)

be = bind_event
