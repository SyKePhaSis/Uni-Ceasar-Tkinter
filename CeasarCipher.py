#Changes:
#   Reorganised Window Management and class functions
#   Binded <Escape> to close Main Window
#   Implemanting _throw_error function to spawn a separete message_box
#   Removing white trailspaces from inputs with .strip()
#   Created Dynamic Lists that can expand accordingly to the user preferences
#   ERROR: If symbol ø not found in list then index = -1 and encrypted_symbol = list[shift - 1] (Fixed)
#   Increased Font size for Ceasar Cipher Info And Window Size (10 -> 18)
#   Added Menu Bar and Created Unicode Mahem

# GUI
import tkinter as tk
from tkinter import messagebox

#Lists
import string

CHAR = [
    "ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩαβγδεζηθικλμνξοπρσςτυφχψω", #ALPHABET_GR
    string.ascii_letters, # APLHABET_EN
    string.digits, #DIGITS
    string.punctuation, #SYMBOLS
    " " #WhiteSpace
]

UNICODE_BOUND = 65535

CHARACTERS_SKIP = [" ", "\t", "\n"]

'''
    Αυτή είναι η κλάση των Γραφικών και στεγάζει ολο το πρόγραμμα μας.
    
    Χρησιμοποιόντας το tkinter και τα functions:
    - _set_objects 
    - _position_objects
    - _set_bindings 
    Kάνει spawn το window και κάνει draw τα γραφικά καθώς και 
    bind το functionality της εφαρμογής μας.

    Η κρυπτογράφιση και αποκρυτογράφιση γίνεται στα functions:
    - encryption
    - decryption
    Αντίστοιχα με την χρήση των Helper Functions:
    - _throw_error (Για την διαχείρηση των σφαλμάτων που μπορούν να εμφανιστούν) 
    - _validate_shift (Για τον έλεγχο του αν ο χρήστης εισήγαγε σωστά στοιχεία στο πεδίο Shift)

    Τέλος υπάρχει και το Info Button οπου μας δίνει μερικές πληροφορίες για το πρόγραμμα μας.
'''
class Graphics():

    def __init__(self):
        self.w = tk.Tk()
        self.w.title("Ceasar's Cryprografy")
        self.w.geometry("800x800")
        self.list = ""
        self.list_settings = [tk.BooleanVar() for i in range(5)]
        self.unicode_mode = tk.BooleanVar()
        self._set_objects()
        self._position_objects()
        self._set_bindings()
        self._create_menubar()
        self.w.mainloop()

    def _set_objects(self):

        self.l1 = tk.Label(self.w, text="What do you want to encrypt?:", font="Times 16")
        self.e1 = tk.Text(self.w, width=40, height=10)
        self.l2 = tk.Label(self.w, text="Give a shift:", font="Times 16")
        self.e2 = tk.Text(self.w, width=10, height=1)
        self.b1 = tk.Button(self.w, text="Press to encode", command=self.encryption, bg="red", font="Times 14")

        self.l3 = tk.Label(self.w, text="What do you want to decrypt?:", font="Times 16")
        self.e3 = tk.Text(self.w, width=40, height=10)
        self.l4 = tk.Label(self.w, text="Give a shift:", font="Times 16")
        self.e4 = tk.Text(self.w, width=10, height=1)
        self.b2 = tk.Button(self.w, text="Press to decode", command=self.decryption, bg="green", font="Times 14")
        self.result = tk.Text(self.w, width=90, height= 10)
        self.just_str = tk.Label(self.w, text="Result:", font="Times 16")
        self.infobutton = tk.Button(self.w, text="Clik to learn more about Caesar cipher!", bg="yellow", font="Times 12", command=self.info_button)

    def _position_objects(self):
        self.l1.place(x=50, y=75)
        self.e1.place(x=50, y=130)
        self.l2.place(x=90, y=350)
        self.e2.place(x=200, y=350)
        self.b1.place(x=150, y=420)
        self.l3.place(x=425, y=75)
        self.e3.place(x=400, y=130)
        self.l4.place(x=415, y=350)
        self.e4.place(x=525, y=350)
        self.b2.place(x=475, y=420)
        self.just_str.place(x=50, y=500)
        self.result.place(x=50, y=540)
        self.infobutton.place(x=500,y=730)
    
    def _set_bindings(self):
        self.w.bind("<Escape>", lambda evnt: self.w.destroy())
        self.b1.bind("<Enter>", lambda evnt: self.b1.configure(bg="white"))
        self.b1.bind("<Leave>", lambda evnt: self.b1.configure(bg="red"))
        self.b2.bind("<Enter>", lambda evnt: self.b2.configure(bg="white"))
        self.b2.bind("<Leave>", lambda evnt: self.b2.configure(bg="green"))

    def info_button(self):
        new_window=tk.Toplevel()
        new_window.geometry("1000x200")
        new_window.title("Caesar cipher info")
        new_text = tk.Label(new_window,text="In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher,"+"\n"
                                            " Caesar's code, or Caesar shift, is one of the simplest and most widely known encryption"+"\n"
                                            " techniques. It is a type of substitution cipher in which each letter in the plaintext is"+"\n"
                                            " replaced by a letter some fixed number of positions down the alphabet. For example, with"+"\n"
                                            " a left shift of 3, D would be replaced by A, E would become B, and so on. The method is"+"\n"
                                            " named after Julius Caesar, who used it in his private correspondence.",font="Times 18")
        new_text.pack()

    def _create_menubar(self):

        #Setting Menu Bar
        menubar = tk.Menu()
        self.w.config(menu = menubar)

        #Set Default Values
        for x in self.list_settings:
            x.set(True)

        self._manage_character_list()

        #Creting Settings Menu
        settings_menu = tk.Menu()
        settings_menu.add_checkbutton
        settings_menu.add_checkbutton(label="Greek", onvalue = 1, offvalue = 0, variable=self.list_settings[0], command = self._manage_character_list)
        settings_menu.add_checkbutton(label="English",onvalue = 1, offvalue = 0, variable=self.list_settings[1], command = self._manage_character_list)
        settings_menu.add_checkbutton(label="Digit", onvalue = 1, offvalue = 0, variable=self.list_settings[2], command = self._manage_character_list)
        settings_menu.add_checkbutton(label="Symbols", onvalue = 1, offvalue = 0, variable=self.list_settings[3], command = self._manage_character_list)
        settings_menu.add_checkbutton(label="Whitespace", onvalue = 1, offvalue = 0, variable=self.list_settings[4], command = self._manage_character_list)

        #Creating Mode Menu
        mode_menu = tk.Menu()
        mode_menu.add_checkbutton(label="Unicode Mayhem Mode", onvalue = 1, offvalue = 0, variable=self.unicode_mode)

        #Adding Menu to Bar
        menubar.add_cascade(menu=settings_menu, label="List Settings")
        menubar.add_cascade(menu=mode_menu, label = "Mode")

    def _set_mode():
        pass

    def _manage_character_list(self):
        self.list = ""
        for index,x in enumerate(self.list_settings):
            if(x.get()):
                self.list += CHAR[index]

    def _throw_error(self,text):
        tk.messagebox.showerror("Error", text)
    
    def _validate_shift(self, shift):
        if(shift == ''):
            self._throw_error("Error: Please fill the shift entry box with the amount you want to displace the value that is being encrypted")
            return False
        try:
            int(shift)
            return True
        except:
            self._throw_error("Error: Please fill the shift entry box with numbers only.\nNote: All floating point numbers will be converted to Integers")
            return False

    def encryption(self):
        encrypted = ""
        user_string = self.e1.get("1.0", "end-1c").strip()
        shift = self.e2.get("1.0", 'end-1c').strip() # Remove all leading and ending whitespaces
        if(self._validate_shift(shift)):
            for i in user_string:
                if(not self.unicode_mode.get()):
                    index = self.list.find(i)
                    if(index == -1):
                        if(i in CHARACTERS_SKIP):
                            encrypted += i
                            continue
                        self._throw_error(f"Error: Symbol {i} couldn't found in the current character list, with unicode number {ord(i)}.\n Note: This character will be replaced with a whitespace.")
                        encrypted += " "
                        continue
                    encrypted += self.list[(index + int(shift) % len(self.list)) % len(self.list)]
                else:
                    encrypted += chr((ord(i) + int(shift)) % UNICODE_BOUND)
                self.result.delete("1.0", tk.END)
                self.result.insert(tk.INSERT, encrypted)

    def decryption(self):
        decrypted = ""
        user_string = self.e3.get("1.0", "end-1c").strip()
        shift = self.e4.get("1.0", "end-1c").strip() # Remove all leading and ending whitespaces
        if(self._validate_shift(shift)):
                for i in user_string:
                    if(not self.unicode_mode.get()):
                        index = self.list.find(i)
                        if(index == -1):
                            if(i in CHARACTERS_SKIP):
                                decrypted += i
                                continue
                            self._throw_error(f"Error: Symbol {i} couldn't found in the current character list, with unicode number {ord(i)}.\n Note: This character will be replaced with a whitespace.")
                            decrypted += " "
                            continue
                        decrypted += self.list[(index - int(shift) % len(self.list)) % len(self.list)]
                    else:
                        decrypted += chr((ord(i) - int(shift)) % UNICODE_BOUND)
                    self.result.delete("1.0", tk.END)
                    self.result.insert(tk.INSERT, decrypted)

if __name__ == "__main__":
    Graphics()
