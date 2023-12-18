from tkinter import *

LETTERS_EN = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()\""
LETTERS_GR = ""

class Graphics:

    def __init__(self, windowName, width, height):
        self.window = Tk()
        self.font = ("Arial", 15)
        self.window.title(windowName)
        self.window.grid_columnconfigure(0, weight=1)
        self.window.grid_columnconfigure(1, weight=1)
        self.window.geometry(f"{width}x{height}")
        self.styleWindow()
        self.window.mainloop()

    def styleWindow(self):

        #Titles
        Label(self.window, text="Κρυπτογράφιση", font=self.font).place(relx = 0.15, rely = 0.04)
        Label(self.window, text="Αποκρυπτογράφιση", font=self.font).place(relx = 0.65, rely = 0.04)
        Label(self.window, text="Shift", font=self.font).place(relx = 0.5,rely = 0.10, anchor=CENTER)

        #Inputs
        self.e1 = Text(self.window, width = 49)
        self.e1.place(relx = 0.0, rely = 0.18)

        self.e2 = Text(self.window, width = 49)
        self.e2.place(relx = 0.5, rely = 0.18)

        self.se = Entry(self.window, width=25)
        self.se.place(relx = 0.5, rely= 0.13, anchor=CENTER)
        
        #Buttons
        self.b1 = Button(self.window, command=self.encrypt, text="Encrypt", background="Green", foreground="White")
        self.b1.place(relx = 0.25, rely = 0.85, anchor=CENTER)
        self.b2 = Button(self.window, command=self.decrypt, text="Decrypt", background="Red", foreground="White")
        self.b2.place(relx = 0.75, rely = 0.85, anchor=CENTER)


    def encrypt(self):
        encrypted = ""
        userInput = self.e1.get("1.0", END)
        shift = int(self.se.get())
        for i in userInput:
            print(i)
            index = LETTERS_EN.find(i)
            encrypted += LETTERS_EN[(index + shift) % len(LETTERS_EN)]
        self.e2.delete("1.0", END)
        self.e2.insert(INSERT, encrypted)


    def decrypt(selft):
        decrypted = ""
        for i in userInput:
            index = LETTERS_EN.find(i)
            decrypted += LETTERS_EN[(index + shift) % len(LETTERS_EN)]
        pass

    
if __name__ == "__main__":
    g = Graphics("Κρυτπογράφιση και Αποκρυπτογράφιση Καίσαρα", 800, 700)