from tkinter import ttk
from tkinter import *
import tkinter as tk
from tkinter import filedialog

from treeviewFunctions import insertCashgameData,insertTourneyData, tourneyHeaders, cashgameHeaders

import matplotlib.style
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg)
from matplotlib.figure import Figure


# Random values for displaying. Ignore
earnings = [0, -2, 0, 4, 2, 8, 8, 6, 12, 15.50, 17.50, 10, -2, -8]
totalHands = 1022
bb100random = -4
netWonAmount = sum(earnings)
defaultColor = "#f0f0f0"
ROI_value = 10
ROI_value_original = ROI_value
VPIP_amount = 22
PFR_amount = 11
BET3_amount = 7
AGG_PCT_amount = 3
CBET_amount = 2
CBET_Fold_amount = 3

# Variables for window size and screen size
windowWidth = 1300
windowHeight = 800
nw_width = 450
nw_height = 600

# Defining the window and size
win = Tk()

win.title("Poker Tracker")
win.geometry("1300x800")

# Overall theme
s = ttk.Style()
s.theme_use("clam")

# Window is not resizable
win.resizable(False, False)

screenWidth = win.winfo_screenwidth()
screenHeight = win.winfo_screenheight()

# Calculating the center of the screen, in order to correctly place the poker tracker in the center
x_cordinate = int((screenWidth / 2) - (windowWidth / 2))
y_cordinate = int((screenHeight / 2) - (windowHeight / 2))

# Centering the window with the variables above
win.geometry("{}x{}+{}+{}".format(windowWidth, windowHeight, x_cordinate, y_cordinate))

# Function that opens the configure window - Everything regarding that, is contained in here 
def openWindow():
    newWindow = Toplevel(win)
    newWindow.title("Configure")
    newWindow.resizable(False, False)
    nw_x_cordinate = int((screenWidth / 2) - (nw_width / 2))
    nw_y_cordinate = int((screenHeight/ 2) - (nw_height / 2))
    newWindow.geometry("{}x{}+{}+{}".format(450, 600, nw_x_cordinate, nw_y_cordinate)) # Centering

    # Function for opening file browser
    def fileOpener(textfield):
        # Storing file in variable, and changing to string
        f_input = filedialog.askdirectory(initialdir="/")
        f_input_str = str(f_input)

        textfield.insert(tk.END, f_input_str)
        textfield.configure(font=("MoolBoran", 11))

    # Hand History File Explorer 
    Label(newWindow, text="PokerStars Hand History Location").grid(row=0,column=0, sticky=NW, padx=2)
    hh_text = Text(newWindow, height=2, width=43,wrap=NONE)
    hh_text.grid(row=1,column=0,sticky=NW, padx=4)

    hh_button = Button(newWindow, height=1, text="Browse Files", font=("MoolBoran",10), command = lambda:fileOpener(hh_text))
    hh_button.grid(row=1,column=1)

    # Tourn Summary File Explorer 
    Label(newWindow, text="PokerStars Tourn Summary Location").grid(row=2,column=0,sticky=NW,padx=2)
    ts_text = Text(newWindow, height=2, width=43, wrap=NONE)
    ts_text.grid(row=3,column=0,sticky=NW,padx=4)

    ts_button = Button(newWindow, height=2, text="Browse Files", font=("MoolBoran",10), command = lambda:fileOpener(ts_text))
    ts_button.grid(row=3,column=1)

# Menubar
mb = Menu(win)
menu_bar = Menu(mb, tearoff=0)
menu_bar.add_command(label="Configure", command=openWindow)
menu_bar.add_separator()  
menu_bar.add_command(label="Exit", command=win.quit)  

# Add headers/cascades to menubar 
mb.add_cascade(label="File", menu=menu_bar)
win.config(menu=mb)

# Declaring and binding events to the selected tab
tournamentTree = ttk.Treeview(win, show="headings",height=19) #Height should be equal number of MTT's

def on_tab_selected(event):
    selected_tab = event.widget.select()
    tab_text = event.widget.tab(selected_tab, "text")

    if tab_text == "Tournaments":
        for i in tournamentTree.get_children():
            tournamentTree.delete(i)
        insertTourneyData(tournamentTree)
        tourneyHeaders(tournamentTree)

    if tab_text == "Cash Games":
        for i in tournamentTree.get_children():
            tournamentTree.delete(i)
        insertCashgameData(tournamentTree)
        cashgameHeaders(tournamentTree)

# Creating the tab control and the tabs we need
tabControl = ttk.Notebook(win)
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)

tabControl.bind("<<NotebookTabChanged>>", on_tab_selected)

# Adding and naming tab1 and tab2 and finally packing it, making it visible.
tabControl.add(tab1, text="Tournaments")
tabControl.add(tab2, text="Cash Games")
tabControl.pack(expand=1, fill="both")

# Inserting different objects into the different tabs. "Label" can be changed to "Buttons" or "ProgressBar"
ttk.Label(tab2, text="Current Game:", font=("MoolBoran", 11, 'bold')).pack(side=TOP, fill="x")

# Splitting the window into diffrent sections and attaching to tab1.
panedwindow = ttk.Panedwindow(tab1, orient=HORIZONTAL)
panedwindow.pack()

styleFrame1 = ttk.Style()
styleFrame1.configure('My.TFrame', background='#212946')

# Creating the frames and defining their width and height in regards to each other
frame1 = ttk.Frame(panedwindow, width=700, height=460, relief=RIDGE)
frame2 = ttk.Frame(panedwindow, width=545, height=460, relief=RIDGE)

# Here the frames are added to the pane. The weight is like a ratio of their size in regards to eachother.
panedwindow.add(frame1, weight=5)
panedwindow.add(frame2, weight=5)

# Deifing style of graph
matplotlib.style.use("seaborn-dark")
for param in ['figure.facecolor', 'axes.facecolor', 'savefig.facecolor']:
    matplotlib.rcParams[param] = defaultColor  # bluish dark grey
for param in ['text.color', 'axes.labelcolor', 'xtick.color', 'ytick.color']:
    matplotlib.rcParams[param] = '0.9'  # very light grey

# Creating figure, determining size and data. We also create a grid
fig = Figure(figsize=(7.50, 2), dpi=100)
fig.add_subplot().plot(earnings)
ax = fig.gca()
ax.xaxis.label.set_color('black')
ax.yaxis.label.set_color("black")
ax.tick_params(axis='x', colors='black')
ax.tick_params(axis="y", colors="black")
ax.set_xlabel("Total Hands", fontsize=10)
fig.set_facecolor("#dcdad5")
ax.set_facecolor("#dcdad5")
ax.set_ylabel("Won", fontsize=10)
ax.grid(axis="both", color='#2A3459', linestyle='-', linewidth=1)

# Creating canvas for displaying graph
canvas = FigureCanvasTkAgg(fig, frame1)
canvas.draw()

# Displaying the graph with pack
canvas.get_tk_widget().place(relwidth=.95, relheight=.71, x=2, y=3)

# Creating rectangle canvases where we can place text and stats inside
statsCanvas = Canvas(frame1, width=700, height=100, bg="#dcdad5", highlightthickness=0)  # For some reason, it sizes the frames width???

# Key stats section - Label first
ttk.Label(frame1, text="Key Stats", font=("MoolBoran", 11, "bold")).place(relx=.43, rely=0.82,)







# ----------------------------------------Total Hands-----------------------------------------------------------
statsCanvas.pack(side=BOTTOM, fill="x", padx=22, pady=1)  # Ignore - check statsCanvas for comment

totalCardsCanvas = Canvas(frame1, width=80, height=60, bg="#dcdad5", highlightthickness=0)
totalCardsCanvas.create_text(42, 23, fill="#282828", font=("MoolBoran", 14, "bold"), text=str(totalHands))
totalCardsCanvas.create_text(40, 42, fill="#000000", font=("MoolBoran", 10, "bold"), text="Total Hands")
totalCardsCanvas.place(relx=.02299, rely=.86)
# ----------------------------------------Total Hands-----------------------------------------------------------


# ----------------------------------------NET WON-----------------------------------------------------------
# Net Won
netWonTextCanvas = Canvas(frame1, width=80, height=60, bg="#dcdad5", highlightthickness=0)
netWonTextCanvas.create_text(42, 23, fill="#282828", font=("MoolBoran", 14, "bold"), text=str(netWonAmount) + "$")
netWonTextCanvas.create_text(40, 42, fill="#000000", font=("MoolBoran", 10, "bold"), text="Net Won")
netWonTextCanvas.place(relx=.152, rely=.86)
# ----------------------------------------NET WON-----------------------------------------------------------


# ----------------------------------------bb/100 / ROI------------------------------------------------------------
# bb/100 or ROI depending on cahs game/tournament
bb100Canvas = Canvas(frame1, width=80, height=60, bg="#dcdad5", highlightthickness=0)
bb100Canvas.create_text(43, 23, fill="#000000", font=("MoolBoran", 14, "bold"), text=str(bb100random))
bb100Canvas.place(relx=.258, rely=.86)
bb100Label = ttk.Label(bb100Canvas, text="bb/100", font=("MoolBoran", 10, "bold"))
bb100Label.configure(foreground="#000000")
bb100Label.place(relx=.258, rely=.50)
# ----------------------------------------bb/100 / ROI------------------------------------------------------------


# ----------------------------------------CHECKBOX----------------------------------------------------------------
var2 = IntVar()  # Check box state

# Function used for chaining text in the bb100Label
def setText():
    if var2.get() == 1:
        bb100Label.configure(text="  ROI")
    else:
        bb100Label.configure(text="bb/100")

# Creating the Radio buttons, settings its boolean and command function
c2 = ttk.Radiobutton(frame1, text="Tournaments", variable=var2, value=1, command=setText)
c3 = ttk.Radiobutton(frame1, text="Cash Game", variable=var2, value=2, command=setText)
c2.place(relx=.47 - 0.046, rely=.76, anchor="center")
c3.place(relx=.599 - 0.046, rely=.76, anchor="center")
c2.invoke()  # By invoking c2, it will be automatically checked
# ----------------------------------------CHECKBOX------------------------------------------------------------


# ----------------------------------------VPIP------------------------------------------------------------
VPIP_Canvas = Canvas(frame1, width=80, height=60, bg="#dcdad5", highlightthickness=0)
VPIP_Canvas.create_text(41, 23, fill="#282828", font=("MoolBoran", 14, "bold"), text=str(VPIP_amount))
VPIP_Canvas.create_text(40, 42, fill="#000000", font=("MoolBoran", 10, "bold"), text="VPIP")
VPIP_Canvas.place(relx=.354, rely=.86)
# ----------------------------------------VPIP------------------------------------------------------------

# ----------------------------------------PFR------------------------------------------------------------
PFR_Cavnas = Canvas(frame1, width=80, height=60, bg="#dcdad5", highlightthickness=0)
PFR_Cavnas.create_text(40, 23, fill="#282828", font=("MoolBoran", 14, "bold"), text=str(PFR_amount))
PFR_Cavnas.create_text(40, 42, fill="#000000", font=("MoolBoran", 10, "bold"), text="PFR")
PFR_Cavnas.place(relx=.443, rely=.86)
# ----------------------------------------PFR-----------------------------------------------------------------


# ----------------------------------------3BET----------------------------------------------------------------
BET3_Canvas = Canvas(frame1, width=80, height=60, bg="#dcdad5", highlightthickness=0)
BET3_Canvas.create_text(40, 23, fill="#282828", font=("MoolBoran", 14, "bold"), text=str(BET3_amount))
BET3_Canvas.create_text(40, 42, fill="#000000", font=("MoolBoran", 10, "bold"), text="3BET")
BET3_Canvas.place(relx=.529, rely=.86)
# ----------------------------------------3BET----------------------------------------------------------------


# ----------------------------------------AGG%----------------------------------------------------------------
AGG_PCT_Canvas = Canvas(frame1, width=80, height=60, bg="#dcdad5", highlightthickness=0)
AGG_PCT_Canvas.create_text(41, 23, fill="#282828", font=("MoolBoran", 14, "bold"), text=str(AGG_PCT_amount) + "%")
AGG_PCT_Canvas.create_text(40, 42, fill="#000000", font=("MoolBoran", 10, "bold"), text="AGG%")
AGG_PCT_Canvas.place(relx=.620, rely=.86)
# ----------------------------------------AGG%----------------------------------------------------------------



# ----------------------------------------CBET FLOP------------------------------------------------------------
CBET_Canvas = Canvas(frame1, width=80, height=60, bg="#dcdad5", highlightthickness=0)
CBET_Canvas.create_text(41, 23, fill="#282828", font=("MoolBoran", 14, "bold"), text=str(CBET_amount))
CBET_Canvas.create_text(40, 42, fill="#000000", font=("MoolBoran", 10, "bold"), text="C-Bet Flop")
CBET_Canvas.place(relx=.731, rely=.86)
# ----------------------------------------CBET FLOP------------------------------------------------------------


# ----------------------------------------CBET FOLD------------------------------------------------------------
CBET_Fold_Canvas = Canvas(frame1, width=80, height=60, bg="#dcdad5", highlightthickness=0)
CBET_Fold_Canvas.create_text(41, 23, fill="#282828", font=("MoolBoran", 14, "bold"), text=str(CBET_Fold_amount))
CBET_Fold_Canvas.create_text(40, 42, fill="#000000", font=("MoolBoran", 10, "bold"), text="C-Bet Fold")
CBET_Fold_Canvas.place(relx=.857, rely=.86)
# ----------------------------------------CBET FOLD------------------------------------------------------------

# ----------------------------------------Hands Won------------------------------------------------------------
# Maybe implement this later
# ----------------------------------------Hands Won------------------------------------------------------------


ttk.Label(frame2, text="Recent Hand History", font=("MoolBoran", 11, "bold")).place(relx=0.01,rely=0.01)




# Total earnings label
ttk.Label(frame1, text="Total Earnings ($)", font=("MoolBoran", 11, 'bold')).pack(side=TOP, pady=7)

# Separator
separator1 = ttk.Separator(frame1, orient="horizontal")
separator1.place(relx=0, rely=0.798, relwidth=1, relheight=0)


# Tree view - Inserting all data from here
tournamentTree['columns']=("Header1", "Header2", "Header3", "Header4","Header5","Header6","Header7", "Header8")
tournamentTree.column("#0", width=0, stretch=NO)
# Pack tree
tournamentTree.pack()

# Adding vertical scrollbar - Theme cannot be changed, as its window native scrollbar. 
vsb = Scrollbar(win, orient="vertical", command=tournamentTree.yview)
vsb.place(relx=0.985, rely=0.645, relheight=0.352, relwidth=0.015)
tournamentTree.configure(yscrollcommand=vsb.set)


# Columns
tournamentTree.column("Header1", anchor=CENTER, width=161)
tournamentTree.column("Header2", anchor=CENTER, width=161)
tournamentTree.column("Header3", anchor=CENTER, width=161)
tournamentTree.column("Header4", anchor=CENTER, width=161)
tournamentTree.column("Header5", anchor=CENTER, width=161)
tournamentTree.column("Header6", anchor=CENTER, width=161)
tournamentTree.column("Header7", anchor=CENTER, width=162)
tournamentTree.column("Header8", anchor=CENTER, width=162)


# Headings
#tournamentTree.heading("#0", text="", anchor=CENTER)
#tournamentTree.heading("Header1", text="Date", anchor=CENTER)
#tournamentTree.heading("Header2", text="Tournament Description", anchor=CENTER)
#tournamentTree.heading("Header3", text="Game")
#tournamentTree.heading("Header4", text="Buy-In", anchor=CENTER)
#tournamentTree.heading("Header5", text="Net Won", anchor=CENTER)
#tournamentTree.heading("Header6", text="Prize Pool", anchor=CENTER)
#tournamentTree.heading("Header7", text="Players", anchor=CENTER)
#tournamentTree.heading("Header8", text="Placement", anchor=CENTER)




# Eventually we can insert data like this:
#for tourn in tourns:
    #tree.insert('', tk.END, values=tourn)




# Tkinter loop
win.mainloop()
