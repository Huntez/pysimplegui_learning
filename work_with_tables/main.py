import PySimpleGUI as sg
import contact_window

sg.theme('Black')

layout = [[sg.Text('ID'), sg.Input(size=(2,1), key='ID')],
          [sg.Text('Enter full name:'), sg.Input(size=(20,1), key='Name')],
          [sg.Text('Enter address:'), sg.Input(size=(20,1), key='Address')],
          [sg.Text('Etner phone number'), sg.Input(size=(20,1), key='Phnumber')],
          [sg.Button('Submit Contact Information', key='Submit'), sg.Button('Show Table', key='Show'), sg.Exit()]
          ]

contact_informaton_array = []
headings = ['ID','Name', 'Address', 'Phone number']

window = sg.Window('Contact information', layout)

while True:
    events, values = window.read()
    
    if events in (sg.WIN_CLOSED, 'Exit'):
        break
    elif events == 'Submit':
        info = [values['ID'], values['Name'], values['Address'], values['Phnumber']]
        contact_informaton_array.append(info)
    elif events == 'Show':
        contact_window.create(contact_informaton_array, headings)

window.close()