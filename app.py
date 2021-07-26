from tkinter import *
from threading import Thread
from queue import Queue
from custom_modules.index import window_event_handler, save_to_file, cls, save_content_to_file_requirements, be, STATUS_MESSENGER, MESSENGER_SWITCH
from classes.index import WebSearcher

cls()

root = Tk()
root.title("General App")
root.minsize(550, 100)
root.maxsize(550, 100)
window_event_handler(root)


search_entry_var = StringVar()


def save_error_message(arg):
    function = MESSENGER_SWITCH['error']
    function('save error'.title(), arg)


def save_error_message_thread(arg):
    save_error_thread = Thread(target=save_error_message, args=(arg,))
    save_error_thread.start()
    save_error_thread = None


def search_error_message(arg):
    function = MESSENGER_SWITCH['error']
    function("search error".title(), arg)


def search_error_message_thread(arg):
    error_thread = Thread(target=search_error_message, args=(arg,))
    error_thread.start()
    error_thread = None


def search(arg):
    if arg:
        ws = WebSearcher(arg)
        results = ws.make_request('get')
        status = results['status']
        if not status:
            search_error_message_thread(results['error'])
        return results
    else:
        message = STATUS_MESSENGER['error']("Missing argument")
        print("\n\t\t\t{}\n\n".format(message))
        return None


def search_thread():
    que = Queue()
    search_thread = Thread(target=lambda q, args1: q.put(
        search(args1)), args=(que, search_entry_var.get()))
    search_thread.setName('search thread'.title())
    search_thread.start()
    search_thread = None
    result = que.get()
    if result:
        if result['status']:
            content = result['data'].content
            destination = save_content_to_file_requirements()
            if not None == destination:
                save_results = save_to_file(content, destination)
                if save_results['status']:
                    print("\n\t{}\n\n".format(save_results['data'].text))
                else:
                    save_error_message_thread(save_results['error'])
            else:
                return


def button_search_handler(event):
    search_thread()


def button_keyrelease_handler(event):
    if event.keysym == 'space' or event.keycode == 65:
        search_thread()


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
