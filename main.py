from sympy import *
import PySimpleGUI as sg

sg.theme('DarkAmber')

menu_def = [
    ['Help', ['About...', 'Formulas']],
]

layout = [
    [sg.Menu(menu_def, tearoff=False)],
    [sg.Text('Enter below your expression in sympy form:')],
    [sg.InputText("", key='expression', size=(45,1))],
    [sg.HorizontalSeparator()],
    [sg.Output(size=(45,1), key='output')],
    [sg.Button('Translate', key='translate')],
]

window = sg.Window('LaTeX Translator', layout, element_padding=(2,2), resizable=True)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break

    if event == 'translate':
        print(latex(sympify(values['expression'])))

    if event == 'About...':
        sg.popup('About this app:', 'Version 1.0', 'Developed by: Axl Andrade')

    if event =='Formulas':
        sg.popup('Derivative: Derivative(Expression, variable)', 'Integral: Integral(Expression, variable)',
        'Limit: Limit(Expression, variable, ->)', 'To raise a number to a power x: number**x')

window.close()
