from tkinter import filedialog

def insertTourneyData (treeview):
	treeview.insert(parent="", index=0, iid=0, text="", values=("NIGGER/10/22", "Super Satellite MTT", "No Limit Hold'em", "$0.13/$0.01 USD", "$0.00", "$15.47 USD", "90 players", "50th place"))
	"""treeview.insert(parent="", index=1, iid=1, text="", values=("2021/10/22", "MTT 8-Max", "No Limit Hold'em", "$0.98/$0.12 USD", "$0.25", "$547.68 USD", "1141 players", "288th place"))
	treeview.insert(parent='', index=2, iid=2, text='', values=("2021/10/07","Super Satellite MTT","No Limit Hold'em", "$0.13/$0.01 USD", "$0.00", "$15.47 USD", "90 players", "50th place"))
	treeview.insert(parent='', index=3, iid=3, text='', values=("2021/10/07","Super Satellite MTT","No Limit Hold'em", "$0.13/$0.01 USD", "$0.00", "$15.47 USD", "90 players", "50th place"))
	treeview.insert(parent='', index=4, iid=4, text='', values=("2021/10/07","Super Satellite MTT","No Limit Hold'em", "$0.13/$0.01 USD", "$0.00", "$15.47 USD", "90 players", "50th place"))
	treeview.insert(parent="", index=5, iid=5, text="", values=("2021/10/07", "Super Satellite MTT", "No Limit Hold'em", "$0.13/$0.01 USD", "$0.00", "$15.47 USD", "90 players", "50th place"))
	treeview.insert(parent="", index=6, iid=6, text="", values=("2021/10/07", "Super Satellite MTT", "No Limit Hold'em", "$0.13/$0.01 USD", "$0.00", "$15.47 USD", "90 players", "50th place"))
	treeview.insert(parent='', index=7, iid=7, text='', values=("2021/10/07","Super Satellite MTT","No Limit Hold'em", "$0.13/$0.01 USD", "$0.00", "$15.47 USD", "90 players", "50th place"))
	treeview.insert(parent='', index=8, iid=8, text='', values=("2021/10/07","Super Satellite MTT","No Limit Hold'em", "$0.13/$0.01 USD", "$0.00", "$15.47 USD", "90 players", "50th place"))
	treeview.insert(parent='', index=9, iid=9, text='', values=("2021/10/07","Super Satellite MTT","No Limit Hold'em", "$0.13/$0.01 USD", "$0.00", "$15.47 USD", "90 players", "50th place"))
	treeview.insert(parent="", index=10, iid=10, text="", values=("2021/10/07", "Super Satellite MTT", "No Limit Hold'em", "$0.13/$0.01 USD", "$0.00", "$15.47 USD", "90 players", "50th place"))
	treeview.insert(parent="", index=11, iid=11, text="", values=("2021/10/07", "Super Satellite MTT", "No Limit Hold'em", "$0.13/$0.01 USD", "$0.00", "$15.47 USD", "90 players", "50th place"))
	treeview.insert(parent='', index=12, iid=12, text='', values=("2021/10/07","Super Satellite MTT","No Limit Hold'em", "$0.13/$0.01 USD", "$0.00", "$15.47 USD", "90 players", "50th place"))
	treeview.insert(parent='', index=13, iid=13, text='', values=("2021/10/07","Super Satellite MTT","No Limit Hold'em", "$0.13/$0.01 USD", "$0.00", "$15.47 USD", "90 players", "50th place"))
	treeview.insert(parent='', index=14, iid=14, text='', values=("2021/10/07","Super Satellite MTT","No Limit Hold'em", "$0.13/$0.01 USD", "$0.00", "$15.47 USD", "90 players", "50th place"))
	treeview.insert(parent="", index=15, iid=15, text="", values=("2021/10/07", "Super Satellite MTT", "No Limit Hold'em", "$0.13/$0.01 USD", "$0.00", "$15.47 USD", "90 players", "50th place"))
	treeview.insert(parent="", index=16, iid=16, text="", values=("2021/10/07", "Super Satellite MTT", "No Limit Hold'em", "$0.13/$0.01 USD", "$0.00", "$15.47 USD", "90 players", "50th place"))
	treeview.insert(parent='', index=17, iid=17, text='', values=("2021/10/07","Super Satellite MTT","No Limit Hold'em", "$0.13/$0.01 USD", "$0.00", "$15.47 USD", "90 players", "50th place"))
	treeview.insert(parent='', index=18, iid=18, text='', values=("2021/10/07","Super Satellite MTT","No Limit Hold'em", "$0.13/$0.01 USD", "$0.00", "$15.47 USD", "90 players", "50th place"))
	treeview.insert(parent='', index=19, iid=19, text='', values=("2021/10/07","Super Satellite MTT","No Limit Hold'em", "$0.13/$0.01 USD", "$0.00", "$15.47 USD", "90 players", "50th place"))"""

def tourneyHeaders(treeview):
	treeview.heading("#0", text="")
	treeview.heading("Header1", text="Date")
	treeview.heading("Header2", text="Tournament Description")
	treeview.heading("Header3", text="Game")
	treeview.heading("Header4", text="Buy-In")
	treeview.heading("Header5", text="Net Won")
	treeview.heading("Header6", text="Prize Pool")
	treeview.heading("Header7", text="Players")
	treeview.heading("Header8", text="Placement")

def cashgameHeaders(treeview):
	treeview.heading("#0", text="")
	treeview.heading("Header1", text="Table")
	treeview.heading("Header2", text="Stake")
	treeview.heading("Header3", text="Game")
	treeview.heading("Header4", text="Won")
	treeview.heading("Header5", text="Hands")
	treeview.heading("Header6", text="Hands Won")
	treeview.heading("Header7", text="Sessions")
	treeview.heading("Header8", text="BB/100")

def insertCashgameData (treeview):
	treeview.insert(parent="", index=0, iid=0, text="", values=("Halley", "Super Satellite MTT", "No Limit Hold'em", "$0.13/$0.01 USD", "$0.00", "$15.47 USD", "90 players", "50th place"))
"""	treeview.insert(parent="", index=1, iid=1, text="", values=("2021/10/22", "MTT 8-Max", "No Limit Hold'em", "$0.98/$0.12 USD", "$0.25", "$547.68 USD", "1141 players", "288th place"))
	treeview.insert(parent='', index=2, iid=2, text='', values=("2021/10/07","Super Satellite MTT","No Limit Hold'em", "$0.13/$0.01 USD", "$0.00", "$15.47 USD", "90 players", "50th place"))
	treeview.insert(parent='', index=3, iid=3, text='', values=("2021/10/07","Super Satellite MTT","No Limit Hold'em", "$0.13/$0.01 USD", "$0.00", "$15.47 USD", "90 players", "50th place"))
	treeview.insert(parent='', index=4, iid=4, text='', values=("2021/10/07","Super Satellite MTT","No Limit Hold'em", "$0.13/$0.01 USD", "$0.00", "$15.47 USD", "90 players", "50th place"))
	treeview.insert(parent="", index=5, iid=5, text="", values=("2021/10/07", "Super Satellite MTT", "No Limit Hold'em", "$0.13/$0.01 USD", "$0.00", "$15.47 USD", "90 players", "50th place"))
	treeview.insert(parent="", index=6, iid=6, text="", values=("2021/10/07", "Super Satellite MTT", "No Limit Hold'em", "$0.13/$0.01 USD", "$0.00", "$15.47 USD", "90 players", "50th place"))
	treeview.insert(parent='', index=7, iid=7, text='', values=("2021/10/07","Super Satellite MTT","No Limit Hold'em", "$0.13/$0.01 USD", "$0.00", "$15.47 USD", "90 players", "50th place"))
	treeview.insert(parent='', index=8, iid=8, text='', values=("2021/10/07","Super Satellite MTT","No Limit Hold'em", "$0.13/$0.01 USD", "$0.00", "$15.47 USD", "90 players", "50th place"))
	treeview.insert(parent='', index=9, iid=9, text='', values=("2021/10/07","Super Satellite MTT","No Limit Hold'em", "$0.13/$0.01 USD", "$0.00", "$15.47 USD", "90 players", "50th place"))
	treeview.insert(parent="", index=10, iid=10, text="", values=("2021/10/07", "Super Satellite MTT", "No Limit Hold'em", "$0.13/$0.01 USD", "$0.00", "$15.47 USD", "90 players", "50th place"))
	treeview.insert(parent="", index=11, iid=11, text="", values=("2021/10/07", "Super Satellite MTT", "No Limit Hold'em", "$0.13/$0.01 USD", "$0.00", "$15.47 USD", "90 players", "50th place"))
	treeview.insert(parent='', index=12, iid=12, text='', values=("2021/10/07","Super Satellite MTT","No Limit Hold'em", "$0.13/$0.01 USD", "$0.00", "$15.47 USD", "90 players", "50th place"))
	treeview.insert(parent='', index=13, iid=13, text='', values=("2021/10/07","Super Satellite MTT","No Limit Hold'em", "$0.13/$0.01 USD", "$0.00", "$15.47 USD", "90 players", "50th place"))
	treeview.insert(parent='', index=14, iid=14, text='', values=("2021/10/07","Super Satellite MTT","No Limit Hold'em", "$0.13/$0.01 USD", "$0.00", "$15.47 USD", "90 players", "50th place"))
	treeview.insert(parent="", index=15, iid=15, text="", values=("2021/10/07", "Super Satellite MTT", "No Limit Hold'em", "$0.13/$0.01 USD", "$0.00", "$15.47 USD", "90 players", "50th place"))
	treeview.insert(parent="", index=16, iid=16, text="", values=("2021/10/07", "Super Satellite MTT", "No Limit Hold'em", "$0.13/$0.01 USD", "$0.00", "$15.47 USD", "90 players", "50th place"))
	treeview.insert(parent='', index=17, iid=17, text='', values=("2021/10/07","Super Satellite MTT","No Limit Hold'em", "$0.13/$0.01 USD", "$0.00", "$15.47 USD", "90 players", "50th place"))
	treeview.insert(parent='', index=18, iid=18, text='', values=("2021/10/07","Super Satellite MTT","No Limit Hold'em", "$0.13/$0.01 USD", "$0.00", "$15.47 USD", "90 players", "50th place"))
	treeview.insert(parent='', index=19, iid=19, text='', values=("2021/10/07","Super Satellite MTT","No Limit Hold'em", "$0.13/$0.01 USD", "$0.00", "$15.47 USD", "90 players", "50th place"))"""

def removeEntries (treeview):
	for i in treeview.get_children():
		treeview.delete(i)

def handleTabChanged(event):
	removeEntries(treeview)

