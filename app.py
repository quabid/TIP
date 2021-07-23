from tkinter import *
from threading import Thread
from queue import Queue
from custom_modules.index import window_event_handler, cls, be, STATUS_MESSENGER, MESSENGER_SWITCH


cls()

root = Tk()
root.title("General App")
root.minsize(550, 500)
root.maxsize(550, 500)
window_event_handler(root)


search_entry_var = StringVar()


def get_video(arg):
    if arg:
        print("\n\n\t\t\tArgument:\t\t{}".format(arg))
    else:
        message = STATUS_MESSENGER['error']("Missing argument")
        print("\n\t\t\t{}\n\n".format(message))

    return arg.upper()


def init_thread():
    que = Queue()

    video_thread = Thread(target=lambda q, args1: q.put(
        get_video(args1)), args=(que, search_entry_var.get()))

    video_thread.setName('video downloader thread'.title())

    print("\t\t\tSeparate Thread: {}".format(video_thread.getName()))

    video_thread.start()
    video_thread = None

    result = que.get()

    if result:
        print("\t\t\tResults:\t\t{}\n\n".format(result))


def button_search_handler(event):
    init_thread()


def button_keyrelease_handler(event):
    print("{} KeyRelease Event\n\tKey Code: {}\n\tKey Name: {}\n".format(
        event.widget, event.keycode, event.keysym))
    if event.keysym == 'space' or event.keycode == 65:
        init_thread()


def clear_entry_on_focusin(event):
    search_entry_var.set("")


def build_interface():
    # Content pane
    search_frame = LabelFrame(root, text="url".upper())
    search_frame.grid(padx=19, pady=5)

    # Textfield
    search_entry = Entry(search_frame, textvariable=search_entry_var, width=45, font=(
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
