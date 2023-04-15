import PySimpleGUI as sg

def reservation_window(reservations_array, headings):
    reservation_window_layout = [[sg.Table(values=reservations_array, size=(60,10),
                                           justification = 'center',
                                           key='DESTINATION',
                                           headings=headings,
                                           max_col_width=40,
                                           row_height=35,
                                           auto_size_columns=True)],
                                 [sg.Button('Exit')]
                                ]
    reservation_window = sg.Window('Reservation Window', reservation_window_layout)

    event, values = reservation_window.read()

    if event in (sg.WIN_CLOSED, 'Exit'):
        reservation_window.close()

def reserve_ticket(values, reservations_array):

    gender = ''
    if values['MALE']:
        gender = 'MALE'
    else:
        gender = 'FEMALE'

    information = [values['FULLNAME'], values['PASSNUM'],
                   gender, values['DEPERATURE'],
                   values['DATE-OF-ARRIVAL'], values['CITYLIST'][0]]

    reservations_array.append(information)

    