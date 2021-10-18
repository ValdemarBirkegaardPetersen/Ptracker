from tkinter import ttk
from tkinter import *


from CenterWindow import menubar

import matplotlib.style
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg)
from matplotlib.figure import Figure

# Removed setup.py

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


# Defining the window and size
win = Tk()

win.title("Poker Tracker")
win.geometry("1300x800")

# Window is not resizable
win.resizable(False, False)
# Variables for window size and screen size
windowWidth = 1300
windowHeight = 800
screenWidth = win.winfo_screenwidth()
screenHeight = win.winfo_screenheight()

# Calculating the center of the screen, in order to correctly place the poker tracker in the center
x_cordinate = int((screenWidth / 2) - (windowWidth / 2))
y_cordinate = int((screenHeight / 2) - (windowHeight / 2))

# Centering the window with the variables above
win.geometry("{}x{}+{}+{}".format(windowWidth, windowHeight, x_cordinate, y_cordinate))

# Calling external menubar function
menubar(win)
print("here")
print("here")
print("here")
print("here")
# Creating the tab control and the tabs we need
tabControl = ttk.Notebook(win)
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)

# Adding and naming tab1 and tab2 and finally packing it, making it visible.
tabControl.add(tab1, text="Reports")
tabControl.add(tab2, text="Live Play")
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
frame2 = ttk.Frame(panedwindow, width=541, height=460, relief=RIDGE)

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




# PLACE STUFF HERE THAT YOU WANT TO STAY IN FRONT

# Total earnings label
ttk.Label(frame1, text="Total Earnings ($)", font=("MoolBoran", 11, 'bold')).pack(side=TOP, pady=7)

# Separator
separator1 = ttk.Separator(frame1, orient="horizontal")
separator1.place(relx=0, rely=0.798, relwidth=1, relheight=0)


# Tree view - MTT
tournamentTree = ttk.Treeview(win, show="headings",height=8)
tournamentTree['columns']=("Rank", "Name", "Badge")
tournamentTree.column("#0", width=0, stretch=NO)
tournamentTree.column("Rank", anchor=CENTER, width=222)
tournamentTree.column("Name", anchor=CENTER, width=222)
tournamentTree.column("Badge", anchor=CENTER, width=222)

# Headings
tournamentTree.heading("#0", text="", anchor=CENTER)
tournamentTree.heading("Rank", text="Id", anchor=CENTER)
tournamentTree.heading("Name", text="Rank", anchor=CENTER)
tournamentTree.heading("Badge", text="Badge", anchor=CENTER)

# Insert MTT data here
tournamentTree.insert(parent="", index=0, iid=0, text="", values=("1", "Vineet", "Alpha"))
tournamentTree.insert(parent="", index=1, iid=1, text="", values=("2", "Anil", "Bravo"))
tournamentTree.insert(parent='', index=2, iid=2, text='', values=('3','Vinod','Charlie'))
tournamentTree.insert(parent='', index=3, iid=3, text='', values=('4','Vimal','Delta'))
tournamentTree.insert(parent='', index=4, iid=4, text='', values=('5','Manjeet','Echo'))

s = ttk.Style()
tournamentTree["style"]
s.theme_use("clam")
tournamentTree.place(relx=.002,rely=.609)

# Tree view - Cash Game
tournamentTree = ttk.Treeview(win, show="headings",height=8)
tournamentTree['columns']=("Rank", "Name", "Badge")
tournamentTree.column("#0", width=0, stretch=NO)
tournamentTree.column("Rank", anchor=CENTER, width=222)
tournamentTree.column("Name", anchor=CENTER, width=222)
tournamentTree.column("Badge", anchor=CENTER, width=222)


#treeStyle = ttk.Style()
#treeStyle.theme_use("default")
#treeStyle.map("Treeview")


# Tkinter loop
win.mainloop()
