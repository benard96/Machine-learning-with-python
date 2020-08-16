import tkinter

window=tkinter.Tk()
window.title("Images and icons")

icon=tkinter.PhotoImage(file = "C:/Users/Benard Kimahala/Desktop/photo1.png")
#display the picture using a label

label=tkinter.Label(window, image=icon)
label.pack()

window.mainloop()