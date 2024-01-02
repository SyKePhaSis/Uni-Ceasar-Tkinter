#caesar cipher final
import tkinter as tk

ALPHABET_upper = "!@#$%^&*()QWERTYUIOPASDFGHJKLZXCέύίόά¨ςερτυθιοπασ~`|\δφγη ξκλζχψωβνμΕΡΤΥΘΙΟΠΑΣΔΦΓΗΞΚΛΖΧΨΩΒΝΜήώVBNM:<>?}+{_-=;/.,qwertyuiopa[]sdfghjklzxcv΄bnm1235678'9034f\""


class Grafics():
    # κλάση που ορίζει τα γραφικά
    def __init__(self, root):
        self.w = root
        self.w.title("Ceasar's Cryprografy")
        self.w.geometry("800x800")
        self.l1 = tk.Label(self.w, text="What do you want to encrypt?:", font="Times 16")
        self.e1 = tk.Text(self.w, width=40, height=10)
        self.l2 = tk.Label(self.w, text="Give a shift:", font="Times 16")
        self.e2 = tk.Text(self.w, width=10, height=1)
        self.b1 = tk.Button(self.w, text="Press to encode", command=self.encryption, bg="red", font="Times 14")
        self.b1.bind("<Enter>", self.bind_1)
        self.b1.bind("<Leave>", self.bind_1_new)
        self.l1.place(x=50, y=75)
        self.e1.place(x=50, y=130)
        self.l2.place(x=90, y=350)
        self.e2.place(x=200, y=350)
        self.b1.place(x=150, y=420)
        self.l3 = tk.Label(self.w, text="What do you want to decrypt?:", font="Times 16")
        self.e3 = tk.Text(self.w, width=40, height=10)
        self.l4 = tk.Label(self.w, text="Give a shift:", font="Times 16")
        self.e4 = tk.Text(self.w, width=10, height=1)
        self.b2 = tk.Button(self.w, text="Press to decode", command=self.decryption, bg="green", font="Times 14")
        self.b2.bind("<Enter>", self.bind_2)
        self.b2.bind("<Leave>", self.bind_2_new)
        self.result = tk.Label(self.w, text="", font=100)
        self.just_str = tk.Label(self.w, text="Result:", font="Times 16")
        self.l3.place(x=425, y=75)
        self.e3.place(x=400, y=130)
        self.l4.place(x=415, y=350)
        self.e4.place(x=525, y=350)
        self.b2.place(x=475, y=420)
        self.result.place(x=200, y=600)
        self.just_str.place(x=200, y=600)
        self.infobutton = tk.Button(self.w, text="Clik to learn more about Caesar cipher!", bg="yellow", font="Times 12", command=self.info_button)
        self.infobutton.place(x=500,y=700)

    def info_button(self):
        new_window=tk.Toplevel()
        new_window.geometry("500x200")
        new_window.title("Caesar cipher info")
        new_text = tk.Label(new_window,text="In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher,"+"\n"
                                            " Caesar's code, or Caesar shift, is one of the simplest and most widely known encryption"+"\n"
                                            " techniques. It is a type of substitution cipher in which each letter in the plaintext is"+"\n"
                                            " replaced by a letter some fixed number of positions down the alphabet. For example, with"+"\n"
                                            " a left shift of 3, D would be replaced by A, E would become B, and so on. The method is"+"\n"
                                            " named after Julius Caesar, who used it in his private correspondence.",font="Times 10")
        new_text.pack()

    def bind_1(self, evnt):
        self.b1.configure(bg="white")

    def bind_1_new(self, evnt):
        self.b1.configure(bg="red")

    def bind_2(self, evnt):
        self.b2.configure(bg="white")

    def bind_2_new(self, evnt):
        self.b2.configure(bg="green")

    def encryption(self):
        encrypted = ""
        user_string = self.e1.get("1.0", "end-1c")
        shift = self.e2.get("1.0", 'end-1c')

        while True:
            try:
                for i in user_string:
                    index = ALPHABET_upper.find(i)
                    encrypted += ALPHABET_upper[(index + int(shift) % len(ALPHABET_upper)) % len(ALPHABET_upper)]

                    self.result.configure(text="\n" + encrypted)
                break

            except ValueError:
                self.result.configure(text="please put a number for shift")
                break

    def decryption(self):
        decrypted = ""
        user_string = self.e3.get("1.0", "end-1c")
        shift = self.e4.get("1.0", "end-1c")

        while True:
            try:
                for i in user_string:
                    index = ALPHABET_upper.find(i)
                    decrypted += ALPHABET_upper[(index - int(shift) % len(ALPHABET_upper)) % len(ALPHABET_upper)]

                    self.result.configure(text="\n" + decrypted)
                break

            except ValueError:
                self.result.configure(text="please put a number for shift")
                break


if __name__ == "__main__":
    # user_string = input("What you want to decrypt?:")
    # shift = input("Give a shift:")
    root = tk.Tk()
    Grafics(root)
    root.mainloop()
