# import TKinter
import tkinter

class MyGui:
    def __init__(self):
        # widget for the main window
        self.main_window = tkinter.Tk()
        # test to see if labels work with string variables
        self.var = 'Winken'

        # top of main window
        self.top_frame = tkinter.Frame(self.main_window)
        # bottom of main window
        self.bottom_frame = tkinter.Frame(self.main_window)


        # three labels for top frame
        self.label1 = tkinter.Label(self.top_frame, text = 'Winken')
        self.label2 = tkinter.Label(self.top_frame, text = 'Blinken')
        self.label3 = tkinter.Label(self.top_frame, text = 'Nod')

        # pack the labels
        self.label1.pack(side = 'top')
        self.label2.pack(side = 'top')
        self.label3.pack(side = 'top')

        # three labels for the bottom frame
        self.label4 = tkinter.Label(self.bottom_frame, text = 'Nod')
        self.label5 = tkinter.Label(self.bottom_frame, text = 'Blinken')
        self.label6 = tkinter.Label(self.bottom_frame, text = self.var)

        # pack the labels
        self.label4.pack(side = 'left')
        self.label5.pack(side = 'left')
        self.label6.pack(side = 'left')

        # pack the frames
        self.top_frame.pack()
        self.bottom_frame.pack()

        # enter the main loop
        tkinter.mainloop()


my_gui = MyGui()

