from variables import *


menu(menu3)


while True:                             # Event Loop
	event, values = window.read(timeout = delay)
	if event == "_EXIT_" or event == sg.WIN_CLOSED:
		break
	elif login == False:
		menu(menu3)
		delay = None
		if event == "_LOGIN2_":
			jsondircache = jsondir + "/" + str(values["_LOGINPROMPT_"]) + ".json"
			prevval = values["_LOGINPROMPT_"]
			hello = {
			timeReplaceAppend() : []
			}
			timeReplaceAppend(hello)
			jsonChange("w", hello, jsondircache)
			menu(menu1)
			login = True
		elif str(values["_LOGINPROMPT_"]) == prevval:
			delay = None
		else:
			jsondircache = jsondir + "/" + str(values["_LOGINPROMPT_"]) + ".json"
			prevval = values["_LOGINPROMPT_"]
			hello = {
			timeReplaceAppend() : []
			}
			timeReplaceAppend(hello)
			jsonChange("w", hello, jsondircache)
			menu(menu1)
			login = True
		print(window["_BACK_"])
	elif event == "_LOGOUT_":
		delay = None
		login = False
		menu(menu3)
	elif event == "_GRAPHSTART_":
		graphactive = True
		menu(menu2)
		delay = 500
	elif event == "_READ_":
		readState = True
	elif readState == True:
		delay = None
		graphactive = False
		#work in progress
		menu(menu1)
		readState = False

	elif graphactive == True:
		if event == "_BACK_":
			delay = None
			graphactive = False
			menu(menu1)
			goBack = True
			delay = 500
		y = randint(0,GRAPH_SIZE[1])        # get random point for graph
		if goBack == True:
			delay = None
			if amount != 0:
				window["_GRAPH_"].Move(GRAPH_STEP_SIZE * amount, 0)
				amount = 0
			else:
				goBack = False 
				delay = 500
				window["_GRAPH_"].erase()
				lastx = lasty = y = 0
				x = 2
		elif x < GRAPH_SIZE[0]:               # if still drawing initial width of graph
			window["_GRAPH_"].DrawLine((lastx+2, lasty), (x+2, y), width=1)
			scale(highesty)
			amount += 1
			if y > highesty:
				highesty = y
			timeReplaceAppend(hello, y)
			jsonChange("w", hello, jsondircache)
		else:                               # finished drawing full graph width so move each time to make room
			window["_GRAPH_"].DrawLine((lastx+2, lasty), (x+2, y), width=1)
			window["_GRAPH_"].Move(-GRAPH_STEP_SIZE, 0)
			scale(highesty)
			amount += 1
			x -= GRAPH_STEP_SIZE
			if y > highesty:
				highesty = y
			timeReplaceAppend(hello, y)
			jsonChange("w", hello, jsondircache)
		lastx, lasty = x, y
		x += GRAPH_STEP_SIZE
#	print(graphactive, login, prevval, values["_LOGINPROMPT_"])
window.close()