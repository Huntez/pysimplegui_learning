import PySimpleGUI as sg
import operator

headings = ['Name', 'Class Mark', 'Age', 'Homeroom Class']
data = [
    ['Jason', 12, 18, 'A'],
    ['Mark', 13, 19, 'B'],
    ['Filiph', 14, 20, 'C'],
    ['Sarah', 15, 17, 'D'],
    ['Johny', 15, 20, 'A']
]

sg.theme('Black')

layout = [[sg.Table(values=data, headings=headings,
                    auto_size_columns=True,
                    justification='center',
                    num_rows=10,
                    row_height=35,
                    enable_events=True,
                    font='Justify',
                    max_col_width=25,
                    key='table',
                    expand_x=True,
                    expand_y=True,
                    enable_click_events=True)]
]

window = sg.Window('test', layout, ttk_theme='clam', resizable=True)

def sort_table(data, col_num_clicked):
    try:
        table_data = sorted(data, key=operator.itemgetter(col_num_clicked))
    except Exception as e:
        print(e)
    else:
        return table_data

while True:
    events, values = window.read()

    print(events)

    if events == sg.WIN_CLOSED:
        break

    if isinstance(events, tuple):
        if events[0] == 'table':
            if events[2][0] == -1 and events and events[2][1] != -1:
                col_num_clicked = events[2][1]
                new_table = sort_table(data, col_num_clicked)
                window['table'].update(new_table)

window.close()