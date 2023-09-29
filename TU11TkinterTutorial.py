import tkinter 
import random

window = tkinter.Tk()


def RandomName():
     names = ["Ashlyn","Owen","Shermaine","David","Harry","Howie"]
     MyName = random.choice(names)
     dice_thrown.configure(text="Name Selected: " + MyName)
     
MyTitle = tkinter.Label(window, text="Random Name Generator",font="Helvetica 16 bold")
MyTitle.pack()

MyButton = tkinter.Button(window, text="OK", command=RandomName)
MyButton.pack()

dice_thrown = tkinter.Label(window, font="Helvetica 16 bold")
dice_thrown.pack()

window.mainloop()
