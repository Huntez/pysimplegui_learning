import PySimpleGUI as sg

sg.theme('black')

def create(contact_information_array, headings):
    layout = [[sg.Table(values=contact_information_array, headings=headings, auto_size_columns=True,
                        display_row_numbers=True,
                        num_rows=20,
                        key='Table',
                        row_height=20,
                        justification='center',
                        enable_events=True,
                        vertical_scroll_only=False)],
                        [sg.Button('Delete')],
                        ]

    window = sg.Window('Contact information', layout, modal=True)

    while True:
        events, values = window.read()

        print('test ' + str(values['Table']))

        if events == 'Table':
            print(values['Table'])

            # contact_information = contact_information_array[values['Table'][0]]
            # sg.popup('test', *contact_information)
        if events == sg.WIN_CLOSED:
            break
        if values['Table'] and events == 'Delete':
            contact_information_array.pop(values['Table'][0])
            window['Table'].update(contact_information_array)

            