import tkinter

window=tkinter.Tk()
window.title("kilometer calculator")
window.minsize(width=300,height=300)

#functionality
def changed():
    try:
        m = int(input_1.get())
        km = round(m / 1000,2)
        my_km.set(str(km))
    except ValueError:
        my_km.set("error")

#label
label=tkinter.Label(text="is equal to",font=("arial",16,"normal"))
label.grid(column=0,row=1)

label1=tkinter.Label(text="Meter",font=("arial",10,"bold"))
label1.grid(column=2,row=0)

label2=tkinter.Label(text="Kilo meter",font=("arial",10,"bold"))
label2.grid(column=2,row=1)
#input for meters
input_1=tkinter.Entry(width=5)
input_1.focus()
input_1.grid(column=1,row=0)


#output for km
my_km=tkinter.StringVar()
my_km.set("0")
output=tkinter.Entry(textvariable=my_km,state="disabled",width=5).grid(column=1,row=1)

#button
button=tkinter.Button(text="change",command=changed)
button.grid(column=1,row=2)

window.mainloop()
