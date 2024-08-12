#passing any  numbers and add them and give the output:
# def add(*args):
#     sum=0
#     for n in args:
#         sum+=n
#     return sum

# print(add(1,2,3,4))
import tkinter
window=tkinter.Tk()
window.title("Hello")
window.minsize(width=500,height=500)
#label
label=tkinter.Label(text="hello",font=("arial",24,"bold"))
label.pack()
#functionality
def clicking():
    label["text"]="lol you clicked it 😭"
    label.config(text="lol you clicked it ")
#button
button=tkinter.Button(text="click me",command=clicking)
button.pack()

window.mainloop()
