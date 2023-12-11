from tkinter import *

class Graphics:

    def __init__(self, windowName, width, height):
        self.window = Tk()
        self.window.title(windowName)
        self.window.grid_columnconfigure(0, weight=1)
        self.window.grid_columnconfigure(1, weight=1)
        # self.window.grid_rowconfigure(0, weight=0)
        self.window.geometry(f"{width}x{height}")
        self.styleWindow()
        self.window.mainloop()

    def styleWindow(self):

        #Main Titlte
        Label(self.window, text="Ceaser Cipher").grid(row = 0, column = 0, columnspan = 2,sticky="ew")

        #Ceasar Title
        Label(self.window, text="Κρυπτογράφιση!").grid(row = 1, column = 0, sticky= "we")
        Label(self.window, text="Αποκρυπτογράφιση!").grid(row = 1, column = 1, sticky="ns")
        

if __name__ == "__main__":
    g = Graphics("Κρυτπογράφιση και Αποκρυπτογράφιση", 500, 500)