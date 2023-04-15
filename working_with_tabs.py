import PySimpleGUI as sg

contact_information_array = [['Amith', '31 Main St.', '667898']]
heading = ['Full Name', 'Street', 'Number']

sg.theme('Black')

information_layout = [[sg.Table(values=contact_information_array, headings=heading,
                                justification='center',
                                max_col_width=35,
                                num_rows=10,
                                row_height=35,
                                key='info_table',
                                display_row_numbers=True)]]

text_layout = [[sg.Text('Just text')]]

form_layout = [[sg.Text('Enter name:'), sg.Input(key='name')],
               [sg.Text('Enter street:'), sg.Input(key='street')],
               [sg.Text('Enter number:'), sg.Input(key='Number')],
               ]

tab_group = [[sg.TabGroup([[sg.Tab('Instructions', text_layout, background_color='Green')],
                           [sg.Tab('Enter contact information', form_layout, element_justification='center')],
                           [sg.Tab('Information layout', information_layout, element_justification='center')]],
                           tab_location='centertop')],
                           [sg.Button('Exit')]
                           ]

window = sg.Window('test', tab_group)

while True:
    events, values = window.read()

    if events in (sg.WIN_CLOSED, 'Exit'):
        break

window.close()