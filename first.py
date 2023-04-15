import PySimpleGUI as sg


sg.theme("Black")

layout = [
    [sg.Text('My first window')],
    [sg.InputText(key='NAME')],
    [sg.InputText(key='RADIUS')],
    [sg.Submit(), sg.Cancel()]
]

window = sg.Window('New window', layout)

while True:
    events, values = window.read()
    
    if events == 'Cancel':
        break
    sg.popup('Test', f'NAME - {values["NAME"]} RADIUS - {values["RADIUS"]}')