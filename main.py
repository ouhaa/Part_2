import tkinter as tk
from tkinter import ttk
import threading
from random import random, randint
from time import sleep
import matplotlib.pyplot as plt

root = tk.Tk() # On crée la fenêtre.
root.title("Robots") # On lui donne un titre.
root.iconname("Robots") # On lui donne un titre.
root.resizable(False, False) # On l'empêche d'être redimensionnée.

button = tk.Button(root, text="Lancer", command=lambda: Canvas())
button.pack(side=tk.BOTTOM)

water = None

Agents = []
dataCollectionList = []

def createAgents(quantité, type, canvas):
    for i in range(quantité):
        position_x, position_y = randint(0, 300), randint(0, 300)
        if type == "Devil":
            canvas.create_oval(position_x, position_y, position_x+20, position_y+20, fill="yellow")


def Canvas():
    global Agents
    global water

    canvas = tk.Canvas(root, width=500, height=500, bg="grey")
    canvas.pack(side=tk.RIGHT)

    water = canvas.create_oval(300, 300, 10+50, 10+200, fill="blue")
    Agents.append(water)

    devil = canvas.create_oval(0, 0, 10, 10, fill="yellow")
    Agents.append(devil)

    thread = threading.Thread(target = MoveDevil, args = (canvas, devil, 0))
    thread.daemon = True
    thread.start()

def MoveDevil(canvas, devil, speed):
    (leftPos, topPos, rightPos, bottomPos) = canvas.coords(devil)

    for overlapping_agent in canvas.find_overlapping(leftPos, topPos, rightPos, bottomPos):
        if overlapping_agent == water:
            return

    button = tk.Button(root, text="go water", command=lambda: MoveDevil(canvas, devil, 50))
    button.pack(side=tk.TOP)

    dataCollectionList.append({"X": (leftPos + rightPos)/2, "Y": (bottomPos + topPos)/2})

    #(waterLeftPos, waterTopPos, waterRightPos, waterBottomPos) = canvas.coords(water)

    #(agentCenterX, agentCenterY) = ((leftPos + rightPos) / 2, (topPos + bottomPos) / 2)
    #(waterCenterX, waterCenterY) = ((waterLeftPos + waterRightPos) / 2, (waterTopPos + waterBottomPos) / 2)

    #canvas.move(devil, waterCenterX - agentCenterX, waterCenterY - agentCenterY)
    canvas.move(devil, speed, speed)


  # createAgents(10, "Devil", canvas)


print(Agents)

root.mainloop() # On démarre la fenêtre.
print("Fenêtre fermée. Création du graphe.")

x, y = [], []
for i in dataCollectionList:
    x.append(i["X"])
    y.append(i["Y"])
plt.plot(x, y, label = "Position", color = "blue")
plt.legend()
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Position")
plt.show()