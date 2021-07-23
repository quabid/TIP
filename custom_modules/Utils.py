import os


def cls(): return os.system('clear')


def bind_event(target, event, method):
    if type(target) != None and type(event) == str and type(method) == function:
        target.bind("<{}>".format(event), method)


be = bind_event

SERVER_BASE = {
    "syoutube": "https://www.youtube.com",
    "oyoutube": "http://www.youtube.com",
    "syt": "https://wwww.youtube.com",
    "oyt": "http://www.youtube.com"
}
