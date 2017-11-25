# import our required library TK Interface
import tkinter

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        # create a label (widget) to contain 'Hello World'
        self.label_1 = tkinter.Label(self.main_window, text="Hello World!")
        self.label_2 = tkinter.Label(self.main_window, text="This is my GUI.")


        #pack label to make it referencable to the main window
        # left, right, top, bottom place the packed item as far in that direction as possible
        self.label_1.pack()
        self.label_2.pack(side = 'right')

        # enter the main loop of Tkinter()
        tkinter.mainloop()

my_gui = MyGUI()
