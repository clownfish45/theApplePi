import PySimpleGUI as sg
from random import randint
import time

GRAPH_SIZE = (400,200)
GRAPH_STEP_SIZE = 7
amount = 0
delay = 100
goBack = False

hello = ("hello!, here are some buttons")
font = "Silkscreen 11"
sg.change_look_and_feel('DarkBlue14')

statecomplete = False
graphactive = False

layout = [  
            [sg.Text(hello)],
            [sg.Button("←", key = '_LEFT_', visible = True, size = 100)],
            [sg.Exit(size = 100)],
            [sg.Button("→", key = '_RIGHT_', visible = True, size = 100)],
            [sg.Button("GO BACK", key = '_BACK_', visible = False, size = 100)],
            [sg.Graph(GRAPH_SIZE, (0,0), GRAPH_SIZE, key='_GRAPH_', background_color='lightblue', visible = False),]]

title = "APPLEPI"

window = sg.Window(title, layout, size = (800, 480), element_justification='c', font = "Silkscreen 11", finalize = True)

lastx = lasty = 0
x = 2
while True:                             # Event Loop
    event, values = window.read(timeout = delay)
    if event == 'Exit' or event == sg.WIN_CLOSED:
        break
    elif event == '_RIGHT_':
        sg.popup("right", font = "Silkscreen 11")
    elif event == '_LEFT_':
        graphactive = True


    elif graphactive == True:
        if statecomplete == False:
            window['_RIGHT_'].update(visible = False)
            window['_LEFT_'].update(visible = False)
            window['_BACK_'].update(visible = True)
            window['_GRAPH_'].update(visible = True)
            statecomplete = True
        if event == '_BACK_':
            statecomplete = False
            graphactive = False
            window['_RIGHT_'].update(visible = True)
            window['_LEFT_'].update(visible = True)
            window['_BACK_'].update(visible = False)
            window['_GRAPH_'].update(visible = False)
            goBack = True

        y = randint(0,GRAPH_SIZE[1])        # get random point for graph
        if goBack == True:
            delay = 0
            if amount != 0:
                window['_GRAPH_'].Move(GRAPH_STEP_SIZE * amount, 0)
                amount = 0
            else:
                goBack = False
            delay = 100
            window['_GRAPH_'].erase()
            lastx = lasty = y = 0
            x = 2
        elif x < GRAPH_SIZE[0]:               # if still drawing initial width of graph
            window['_GRAPH_'].DrawLine((lastx, lasty), (x, y), width=1)
            amount += 1
        else:                               # finished drawing full graph width so move each time to make room
            window['_GRAPH_'].DrawLine((lastx, lasty), (x, y), width=1)
            window['_GRAPH_'].Move(-GRAPH_STEP_SIZE, 0)
            amount += 1
            x -= GRAPH_STEP_SIZE
        lastx, lasty = x, y
        x += GRAPH_STEP_SIZE
window.close()