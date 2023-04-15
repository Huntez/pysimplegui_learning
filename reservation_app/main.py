import PySimpleGUI as sg
from reservation_functions import *

sg.theme('Black')

layout = [[sg.Text('Enter full name:'), sg.Input(key=('FULLNAME'), size=(21,1), do_not_clear=True)],
          [sg.Text('Enter your passport number:'), sg.Input(key='PASSNUM',do_not_clear=True, size=(10,1))],
          [sg.Radio('Male', 'RADIO', key='MALE'), sg.Radio('Female', 'RADIO', key='FEMALE')],
          [sg.Input(key='DEPERATURE', size=(20,1)), sg.CalendarButton(
    'DATE OF DEPERATURE', close_when_date_chosen=True, target='DEPERATURE', location=(0,0), no_titlebar=False)],
          [sg.Input(key='DATE-OF-ARRIVAL', size=(20,1)), sg.CalendarButton(
    "DATE OF ARRIVAL", close_when_date_chosen=True, target='DATE-OF-ARRIVAL', location=(0,0), no_titlebar=False)],
          [sg.Text('Choose your destination:', size=(30,1), font='Lucida')],
          [sg.Listbox(values=['Havana', 'Kiyv', 'Otava', 'Paris', 'London'], size=(40,5), key='CITYLIST', select_mode='single')],
          [sg.Button('Reserve Ticket', key='RESERV'), sg.Button('See Reservation', key='RSVCHECK'), sg.Exit()]
          ]

reservations_array = []
headings = ['Name', 'Passport Number', 'Sex', 'Departure date', 
            'Arrival date', 'Destination']

window = sg.Window('airlines reservation', layout)


while True:
    event, values = window.read()

    print(event)

    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    elif event == 'RESERV':
        sg.popup('Ticket reserved', reserve_ticket(values, reservations_array))
        print(reservations_array)
    elif event == 'RSVCHECK':
        reservation_window(reservations_array, headings)

window.close()