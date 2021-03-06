'''
    pip freeze > requirements.txt
    pyi-makespec --onefile Main.py
    pyinstaller Main.spec
'''
import os
import sys
import warnings

import PySimpleGUI as sg
import requests

from Realization import run_wind_error, run_main_wind

warnings.filterwarnings("ignore")


def check_net():
    try:
        response = requests.get("http://www.google.com")
        return True
    except requests.ConnectionError:
        return False


def resource_path(relative):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative)
    return os.path.join(relative)


if __name__ == '__main__':
    ico = resource_path(os.path.join('data', 'new_ico.ico'))
    sg.set_global_icon(ico)

    if check_net():
        run_main_wind()
    else:
        run_wind_error()