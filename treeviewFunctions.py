def insertTourneyData (treeview):
	print("insert here")

def insertCashgameData (treeview):
	print("intert here")

def removeEntries (treeview):
	for i in treeview.get_children():
		treeview.delete(i)

def handleTabChanged(event):
	removeEntries(treeview)

def hello():
	print("hello")