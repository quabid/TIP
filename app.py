from tkinter import *
from threading import Thread
from queue import Queue
from custom_modules.index import window_event_handler, cls, be, STATUS_MESSENGER, MESSENGER_SWITCH
from classes.index import WebSearcher

cls()

root = Tk()
root.title("General App")
root.minsize(550, 100)
root.maxsize(550, 100)
window_event_handler(root)


search_entry_var = StringVar()


def search(arg):
    if arg:
        ws = WebSearcher(arg)
        response = ws.make_request('get')

        if response:
            if response['status']:
                return response
            else:
                return None

    else:
        message = STATUS_MESSENGER['error']("Missing argument")
        print("\n\t\t\t{}\n\n".format(message))
        return None


def init_thread():

    que = Queue()

    search_thread = Thread(target=lambda q, args1: q.put(
        search(args1)), args=(que, search_entry_var.get()))
    search_thread.setName('search thread'.title())
    search_thread.start()
    search_thread = None

    result = que.get()

    if result:        
        if result['status']:
            print("\n\n\t\t\tResults:\t\t{}\n\n".format(result['data'].text))


def button_search_handler(event):
    init_thread()


def button_keyrelease_handler(event):
    if event.keysym == 'space' or event.keycode == 65:
        init_thread()


def clear_entry_on_focusin(event):
    search_entry_var.set("")


def build_interface():
    # Content pane
    search_frame = LabelFrame(root, text="url".upper())
    search_frame.grid(padx=19, pady=5)

    h_scroller = Scrollbar(orient="horizontal")

    # Textfield
    search_entry = Entry(search_frame, xscrollcommand=h_scroller.set, textvariable=search_entry_var, width=45, font=(
        "Helvetica", 12, 'normal'))
    search_entry.grid(ipady=5, pady=5, column=1, row=1)
    search_entry.bind('<FocusIn>', clear_entry_on_focusin)

    # Button
    search_button = Button(search_frame, text="Search",
                           font=("Helvetica", 12, 'bold'))
    search_button.grid(padx=5, ipady=1, column=2, row=1)
    search_button.bind('<ButtonRelease>', button_search_handler)
    search_button.bind('<KeyRelease>', button_keyrelease_handler)


def create_gui():
    build_interface()
    root.mainloop()


create_gui()
