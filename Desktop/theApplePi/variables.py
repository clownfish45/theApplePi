import PySimpleGUI as sg
from datetime import date
import json
from random import randint

font = "Silkscreen 11"
sg.change_look_and_feel("DarkBlue14")
title = "APPLEPI"
prevval = ""
#jsondir = "/home/theapplepi/Documents/theApplePi/userData" ------> jsondir for rpi
jsondir = "/Users/chmy_kh/Documents/theApplePi/userData" #--------> jsondir for mac
graphcol = "lightblue"

GRAPH_SIZE = (400,200)
GRAPH_STEP_SIZE = 15
amount = 0
lasty = y = x = lastx = highesty = 0

goBack = False
readState = False
graphactive = False
login = False
delay = None


menu1 = ["_GRAPHSTART_", "_READ_", "_LOGOUT_"]
menu2 = ["_GRAPHCANVAS_", "_GRAPH_", "_BACK_"]
menu3 = ["_LOGIN1_", "_LOGINPROMPT_", "_LOGIN2_", "_EXIT_"]
emptymenu = []

keylist = menu1 + menu2 + menu3

menustate = {}

for i in range(len(keylist)):
	menustate[keylist[i]] = True


def jsonChange(x, y, z):		#when called if it"s in write or append mode writes (or appends) to the json file (z directory) with y. when in read mode syncs y with json file (z directory).
	if x == "w" or x == "a":	# USED WHEN WORKING WITH EXTERNAL JSON FILE
		with open(z, x) as file:
			json.dump(y, file, indent = 2)
	elif x == "r":
		with open(z, x) as file:
			y = json.load(file)

def timeReplaceAppend(x = None, y = None): ##creates a time variable, if x and y are called appends the y variable to x, the dictionary. USED WHEN WORKING WITH LOCAL DICTIONARY
	if y == None or x == None:
		return str(date.today()).replace("-", "")
	else:
		return x[str(date.today()).replace("-", "")].append(y)

def menu(x):
	nkeylist = []
	nkeylist += keylist
	for i in range(len(x)):
		window[x[i]].update(visible = True)
		window[x[i]].unhide_row()
		menustate[x[i]] = True
	for y in range(len(x)):
		nkeylist.remove(x[y])
	for p in range(len(nkeylist)):
		if menustate[nkeylist[p]] == True:
			window[nkeylist[p]].hide_row()
			window[nkeylist[p]].update(visible = False)
			menustate[nkeylist[p]] = False

def scale(x):
	highest = int(x - (x % 5) + 5)
	if highest != 5:
		for i in range(1, int(highest / 5)):
			if y == 1:
				window["_GRAPHCANVAS_"].DrawLine((0, 10), (4, 10), width = 1)
				window["_GRAPHCANVAS_"].draw_text(location = (6, 10), text = "5", font = "Silkscreen 11", color = "black")
			else:
				window["_GRAPHCANVAS_"].DrawLine((2, 0), (2, highest), width = 1)
				window["_GRAPHCANVAS_"].DrawLine((0, i * 5), (4, i * 5), width = 1)
				window["_GRAPHCANVAS_"].draw_text(location = (6, i * 5), text = str(i * 5), font = "Silkscreen 11", color = "black")


layout = [  
	[sg.Text("hello! enter a username!", key = "_LOGIN1_", visible = False)],
	[sg.InputText(key = "_LOGINPROMPT_", visible = False)],
	[sg.Submit(key = "_LOGIN2_", size = 100, visible = False)],
	[sg.Button("LIVE GRAPH", key = "_GRAPHSTART_", visible = False, size = 100)],
	[sg.Exit(key = "_EXIT_", size = 100, visible = False)],
	[sg.Button("READ MODE", key = "_READ_", visible = False, size = 100)],
	[sg.Button("LOGOUT", key = "_LOGOUT_", visible = False, size = 100)],
	[sg.Graph(canvas_size=(40, 200), graph_bottom_left=(0, 0), graph_top_right=(8, 200), background_color = graphcol, key = "_GRAPHCANVAS_", visible = False), sg.Graph(GRAPH_SIZE, (0,0), GRAPH_SIZE, key="_GRAPH_", background_color = graphcol, visible = False),],
	[sg.Button("GO BACK", key = "_BACK_", visible = False, size = 100)]
	
]


window = sg.Window(title, layout, element_justification = "c", font = "Silkscreen 11", finalize = True)



# size = (800, 480),

#previous version in diff hunk

if __name__ == "__main__":
	sg.Popup("You are not supposed to run this file!")
	exit();




