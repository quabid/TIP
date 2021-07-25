from tkinter import simpledialog
import os
from .FileValidator import isDir


def set_file_name():
    file_name = simpledialog.askstring(
        title="File Name", prompt="What should the file's name be?:")
    return file_name


def set_ext_name():
    ext_name = simpledialog.askstring(title="File's Extension",
                                      prompt="What should the file's extension be?:")


def set_save_destination():
    dest_path = simpledialog.askstring(title="Save Destination",
                                       prompt="Where should I save the file?:")


def save_content_to_file_requirements(name="file", ext=".txt", destination=os.environ('HOME')):
    file_name = name
    ext_name = ext
    dest_path = destination

    if not file_name:
        file_name = set_file_name()

    if not ext_name:
        ext_name = set_ext_name()

    if not isDir(dest_path) or not dest_path:
        dest_path = set_save_destination()

    return "{}{}{}{}".format(dest_path, os.sep, file_name, ext_name)
