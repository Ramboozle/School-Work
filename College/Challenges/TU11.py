import tkinter
import random
window = tkinter.Tk()
names = ['Steve','Simon','Susan','Alex','Eli']
def RandomName():
    MyRandom = names[random.randint(0,4)]
    name_picked.configure(text=str(MyRandom))
MyTitle = tkinter.Label(window, text = "Random Name Generator")
MyTitle.pack()
MyButton = tkinter.Button(window, text = "Generate", command = RandomName)
MyButton.pack()
name_picked = tkinter.Label(window)
name_picked.pack()
window.mainloop()