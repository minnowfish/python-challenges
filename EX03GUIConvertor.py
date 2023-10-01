#UNFINISHED

import tkinter
 
window = tkinter.Tk()
window.wm_title("Bin / Hex / Dec")
Base_Number=""
 
def evaluate(event):
    if Base_Number == "Binary":
        try:
            dec = int(Myentry.get(),2)
            myhex = hex(dec)
            result1.configure(text = "Decimal is: "+str(dec))
            result2.configure(text = "Hex is: "+str(myhex))
        except ValueError:
            result1.configure(text = "Please enter valid binary")
            result2.configure(text = "")
 
    elif Base_Number == "Decimal":
        try:
            dec = int(Myentry.get())
            mybin = bin(dec)
            myhex = hex(dec)
            result1.configure(text = "Binary is: "+str(mybin))
            result2.configure(text = "Hex is: "+str(myhex))
        except ValueError:
            result1.configure(text = "Please enter valid decimal")
            result2.configure(text = "")
 
    elif Base_Number == "Hex":
        try:
            dec =int(Myentry.get(),16)
            mybin = bin(dec)
            result1.configure(text = "Decimal is: "+str(dec))
            result2.configure(text = "Binary is: "+str(mybin))
        except ValueError:
            result1.configure(text = "Please enter valid hexadecimal")
            result2.configure(text = "")
    else:
        result1.configure(text = "Please select a BASE!")
 
def calcStyle():
    global Base_Number
    Base_Number=base.get()
    print(base.get())
 
MyTitle = tkinter.Label(window, text="Bin / Hex / Dec Converter")
MyTitle.pack()
 
Myentry = tkinter.Entry(window)
Myentry.bind("<Return>", evaluate)
Myentry.pack()
 
result1 = tkinter.Label(window, text="1. Choose a base")
result1.pack()
 
result2 = tkinter.Label(window, text="2. Enter a number and press<enter>")
result2.pack()
 
base = tkinter.StringVar()
tkinter.Radiobutton(window, text="Binary", variable=base, value="Binary", command=calcStyle).pack()
tkinter.Radiobutton(window, text="Decimal", variable=base, value="Decimal", command=calcStyle).pack()
tkinter.Radiobutton(window, text="Hex", variable=base, value="Hex", command=calcStyle).pack()
 
window.mainloop()
