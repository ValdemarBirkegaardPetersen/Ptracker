import matplotlib
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


def createGraph(myWindow, input):
    #Creating figure, determining size and data. We also create a grid
    fig = Figure(figsize=(5, 5), dpi=100)
    t = np.arange(0, 3, .01)
    fig.add_subplot().plot(t, 2 * np.sin(2 * np.pi * t))
    ax = fig.gca()
    ax.grid(axis="both", color='#2A3459', linestyle='-', linewidth=1.50)

    #Deifing style of graph
    matplotlib.style.use("seaborn-dark")
    for param in ['figure.facecolor', 'axes.facecolor', 'savefig.facecolor']:
        matplotlib.rcParams[param] = '#212946'  # bluish dark grey
    for param in ['text.color', 'axes.labelcolor', 'xtick.color', 'ytick.color']:
        matplotlib.rcParams[param] = '0.9'  # very light grey

    canvas = FigureCanvasTkAgg(fig, master=myWindow)
    canvas.draw()