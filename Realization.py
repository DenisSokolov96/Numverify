from QueryAPI import *
import PySimpleGUI as sg


# Главное окно
def run_main_wind():
    sg.theme('Light Green')
    list_value = [["", ""]]
    list_headers = ["Название", "Данные"]

    layout = [[sg.Frame('', [
                [sg.Input(key='-NUM-', size=(15, 1), justification='center',
                          disabled_readonly_background_color='lightblue'),
                 sg.Button("Запрос")]])
               ],
              [sg.Table(values=list_value, headings=list_headers, def_col_width=40, max_col_width=80,
                        background_color='lightblue', text_color='Black', auto_size_columns=False,
                        justification='centre', num_rows=5, alternating_row_color='white',
                        key='-TABLE_OUT-', selected_row_colors=('Black', 'lightgray'), row_height=30)
               ]
              ]
    window = sg.Window('Верификация номера', layout)
    while True:
        event, values = window.read()
        if event == "Запрос":
            list_value = create_response(values['-NUM-'])
            window['-TABLE_OUT-'].update(values=list_value)
        if event in (sg.WIN_CLOSED, 'Quit'):
            break
    window.close()


def create_response(number):
    access_key = read_code()
    country_code = "RU"
    list_value = []

    response = getNum(access_key, number, country_code)
    if response['valid'] is True:
        list_value.append(["Номер телефона: ", response['international_format']])
        list_value.append(["Страна: ", response['country_name']])
        list_value.append(["Область / округ: ", response['location']])
        list_value.append(["Компания: ", response['carrier']])
        list_value.append(["Тип сети: ", response['line_type']])
    return list_value


# Вывод окна при отсутствии интернета
def run_wind_error():
    sg.theme('Light Green')
    layout = [[sg.Text("Нет поключения к интернету")]]
    window = sg.Window('Ошибка подключения', layout, size=(400, 100))
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Quit'):
            break
    window.close()


def read_code():
    fileread = open('data/code.txt')
    str = fileread.read()
    return str