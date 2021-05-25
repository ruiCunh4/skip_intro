import tkinter

root= tkinter.Tk()

def skip_cmd():
    exit(0)

pic = tkinter.PhotoImage(file = "Button.png")

root.overrideredirect(1)

myButton = tkinter.Button(root, image = pic, command = skip_cmd)

root.geometry("+1100+650")

myButton.pack()

root.mainloop()