from tkinter import*

root=Tk()


class root(Tk):
    def __init__(self): 
        super(root,self).__init__()
        self.title("Python Tkinter progress bar")
        self.minsize(640, 400)
        
        self.buttonFrame=ttk.LabelFrame(self,text="progress Bar")
        self.buttonFrame.grid(column=0, row=0)
        
        self.progressBar()
        
self,root.mainloop()
        