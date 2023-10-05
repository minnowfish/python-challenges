#UNFINISHED

import tkinter
 
window = tkinter.Tk()
window.wm_title("Celsius, Fahrenheit, Kelvin")
Base_Number=""
 
def evaluate(event):
    if Base_Number == "Celsius":
        try:
            cel = int(Myentry.get(),2)
            myfah = round((cel*1.8)+32,1)
            mykel = cel + 273.15
            result1.configure(text = "Fahrenheit is: "+str(myfah))
            result2.configure(text = "Kelvin is: "+str(mykel))
        except ValueError:
            result1.configure(text = "Please enter valid binary")
            result2.configure(text = "")
 
    elif Base_Number == "Fahrenheit":
        try:
            dec = int(Myentry.get())
            mybin = bin(dec)
            myhex = hex(dec)
            result1.configure(text = "Binary is: "+str(mybin))
            result2.configure(text = "Hex is: "+str(myhex))
        except ValueError:
            result1.configure(text = "Please enter valid decimal")
            result2.configure(text = "")
 
    elif Base_Number == "Kelvin":
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
 
MyTitle = tkinter.Label(window, text="Temperature Converter")
MyTitle.pack()
 
Myentry = tkinter.Entry(window)
Myentry.bind("<Return>", evaluate)
Myentry.pack()
 
result1 = tkinter.Label(window, text="1. Choose a unit")
result1.pack()
 
result2 = tkinter.Label(window, text="2. Enter a number and press<enter>")
result2.pack()
 
base = tkinter.StringVar()
tkinter.Radiobutton(window, text="Celsius", variable=base, value="Celsius", command=calcStyle).pack()
tkinter.Radiobutton(window, text="Fahrenheit", variable=base, value="Fahrenheit", command=calcStyle).pack()
tkinter.Radiobutton(window, text="Kelvin", variable=base, value="Kelvin", command=calcStyle).pack()
 
window.mainloop()
