# GUI
import tkinter as tk
from tkinter import messagebox

#Lists
import string

#Λίστα διαθέσημων λιστών χαρακτήρων
CHAR = [
    "ΑΆΒΓΔΕΈΖΗΉΘΙΊΪΚΛΜΝΞΟΌΠΡΣΤΥΎΫΦΧΨΩαάβγδεέζηήθιίϊΐκλμνξοόπρσςτυύϋΰφχψώ", #ALPHABET_GR
    string.ascii_letters, # APLHABET_EN
    string.digits, #DIGITS
    string.punctuation + "«»", #SYMBOLS
    " " #WhiteSpace
]

#Το upper_limit του unicode_mode 
UNICODE_BOUND = 65535

#Χαρακτήρες που αν συναντίσει το πρόγραμμ δεν επιρεάζει ώστε να παραμείνει το indentation ίδιο.
CHARACTERS_SKIP = [" ", "\t", "\n"]

'''
    Αυτή είναι η κλάση των Γραφικών και στεγάζει ολο το πρόγραμμα μας.
    
    Χρησιμοποιόντας το tkinter και τα functions:
    - _set_objects 
    - _position_objects
    - _set_bindings 
    Kάνει spawn το window και κάνει draw τα γραφικά καθώς και 
    bind το functionality της εφαρμογής μας.Ο λόγος του χωρισμού σε τρείς φάσεις έγινε
    για την καλύτερη κατανόηση και εύκολη ,στοχευμένη αλλαγή οπουδήποτε χρειαστεί.

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
        self.w.title("Ceasar's Cryprografy") # Θέτουμε όνομα παραθύρου
        self.w.geometry("800x800") # Διαστάσεις Παραθύρο
        self.w.resizable(False, False)#Απαγορεύουμε το Resizability στον άξονα x και άξονα y

        # Λίστα χαρακτήρων που θα χρησιμοποιηθούν για την κρυπτογράφιση
        # Η οποία θα οριστεί στο function self._create_menubar() οταν 
        # καλεί η μέθοδος self._manage_character_list()
        self.list = ""

        #Η λίστα με boolean values της κλάσης tkinter που χρησιμοποιούνται για τον ορισμό
        #λιστών χαρακτήρων που θα χρησιμοποιηθούν.
        self.list_settings = [tk.BooleanVar() for i in range(5)]
        
        #Boolean value για το αν ειναι ενεργοποιημένο το unicode mode
        self.unicode_mode = tk.BooleanVar()

        #Μέθοδοι για τη δημιουργία του γραφικού Περιβάλοντος και της λειτουργικότητας του προγράμματος
        self._set_objects()
        self._position_objects()
        self._set_bindings()
        self._create_menubar()

        #Τρέχει το Loop που ξεκινάει το περιβάλλον της εφαρμογής μας
        self.w.mainloop()

    def _set_objects(self):

        """
            Κώδικας για την δημιουργία των πεδίων και τίτλων κρυπτογράφισης
            (Τίτλος, Πεδίο για εισαγωγή του Shift, Πεδίο εισαγωγής text για κρυπτογράφιση, κουμπί που καλεί την διαδικασία κρυπτογράφισης) 
        """
        self.l1 = tk.Label(self.w, text="What do you want to encrypt?:", font="Times 16")
        self.e1 = tk.Text(self.w, width=40, height=10)
        self.l2 = tk.Label(self.w, text="Give a shift:", font="Times 16")
        self.e2 = tk.Text(self.w, width=10, height=1)
        self.b1 = tk.Button(self.w, text="Press to encode", command=self.encryption, bg="red", font="Times 14")

        """
            Κώδικας για την δημιουργία των πεδίων και τίτλων αποκρυπτογράφισης
            (Τίτλος, Πεδίο για εισαγωγή του Shift, Πεδίο εισαγωγής text για αποκρυπτογράφιση, κουμπί που καλεί την διαδικασία αποκρυπτογράφισης) 
        """
        self.l3 = tk.Label(self.w, text="What do you want to decrypt?:", font="Times 16")
        self.e3 = tk.Text(self.w, width=40, height=10)
        self.l4 = tk.Label(self.w, text="Give a shift:", font="Times 16")
        self.e4 = tk.Text(self.w, width=10, height=1)
        self.b2 = tk.Button(self.w, text="Press to decode", command=self.decryption, bg="green", font="Times 14")
        self.result = tk.Text(self.w, width=90, height= 10)

        """
            Κουμπί που ανοίγει το παράθυρο που παρουσιάζει τις πληροφορίες για την Κρυπτογράφιση του Καίσαρα.
        """
        self.just_str = tk.Label(self.w, text="Result:", font="Times 16")
        self.infobutton = tk.Button(self.w, text="Clik to learn more about Caesar cipher!", bg="yellow", font="Times 12", command=self.info_button)

    """
        Η μέθοδος αυτή τοποθετεί όλα τα στοιχεία μας που δημιουργήθηκαν στην μέθοδο _set_objects() 
    """
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
    
    """
        Εδω δημιουργούνται όλα τα bindings των Hover Effects των κουμπιών καθώς και binding για την
        έξοδο απο το πρόγραμμα με την χρήση του κουμπιού <Escape>
    """
    def _set_bindings(self):
        self.w.bind("<Escape>", lambda evnt: self.w.destroy())
        self.b1.bind("<Enter>", lambda evnt: self.b1.configure(bg="white"))
        self.b1.bind("<Leave>", lambda evnt: self.b1.configure(bg="red"))
        self.b2.bind("<Enter>", lambda evnt: self.b2.configure(bg="white"))
        self.b2.bind("<Leave>", lambda evnt: self.b2.configure(bg="green"))

    """
         Με την μέθοδο αυτή κάνει Spawn το παράθυρο που παρουσιάζει μερικές πληροφορίες για την
         κρυπτογράφιση του καίσαρα. Θέτουμε επίσης το όνομα και τις διαστάσεις του καινούργιου παραθύρου.
    """
    def info_button(self):
        info_window=tk.Toplevel()
        info_window.geometry("1000x200")
        info_window.title("Caesar cipher info")
        info_window.resizable(False, False)
        info_window.bind("<Escape>", lambda evnt: info_window.destroy())
        info_text = tk.Label(info_window,text="In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher,"+"\n"
                                            " Caesar's code, or Caesar shift, is one of the simplest and most widely known encryption"+"\n"
                                            " techniques. It is a type of substitution cipher in which each letter in the plaintext is"+"\n"
                                            " replaced by a letter some fixed number of positions down the alphabet. For example, with"+"\n"
                                            " a left shift of 3, D would be replaced by A, E would become B, and so on. The method is"+"\n"
                                            " named after Julius Caesar, who used it in his private correspondence.",font="Times 18")
        info_text.pack()

    """
        Δημιουργεί το Menu που παρατηρείτε στο πάνο μέρος του παραθύρου καθώς και το κάθε υπομενού ξεχωριστά.
    """
    def _create_menubar(self):

        #Setting Menu Bar
        #Είναι το Top-Level Menu
        menubar = tk.Menu()
        self.w.config(menu = menubar)

        #Set Default Values
        #Ορίζουμε όλες τις λίστες χαρακτήρων ενεργές
        for x in self.list_settings:
            x.set(True)

        #Δημιουργία της λίστας τών χαρακτήρων που είναι δεκτοί για κρυπτογράφιση
        self._manage_character_list()

        #Creting Settings Menu
        #Όπου κάθε checkbutton έιναι συνδεμένο με ενα boolean value στην λίστα self.list_settings
        #Επίσης κάθε φορά που παρατηρείτε αλλαγή σε κάποιο checkbutton τρέχει η μέθοδος self._manange_character_list()
        #Ώστε να ξαναοριστεί η λίστα χαρακτήρων (self.list)

        settings_menu = tk.Menu()
        settings_menu.add_checkbutton(label="Greek", onvalue = 1, offvalue = 0, variable=self.list_settings[0], command = self._manage_character_list)
        settings_menu.add_checkbutton(label="English",onvalue = 1, offvalue = 0, variable=self.list_settings[1], command = self._manage_character_list)
        settings_menu.add_checkbutton(label="Digits", onvalue = 1, offvalue = 0, variable=self.list_settings[2], command = self._manage_character_list)
        settings_menu.add_checkbutton(label="Symbols", onvalue = 1, offvalue = 0, variable=self.list_settings[3], command = self._manage_character_list)
        settings_menu.add_checkbutton(label="Whitespace", onvalue = 1, offvalue = 0, variable=self.list_settings[4], command = self._manage_character_list)

        #Creating Mode Menu
        #Παρόμοιο με το Settings Menu με αντίστοιχη μεταβλητή το self.unicode_mode
        #Και επίσης η αλλαγή της μεταβλητής αυτής δεν έχει κάποιο action
        mode_menu = tk.Menu()
        mode_menu.add_checkbutton(label="Unicode Mayhem Mode", onvalue = 1, offvalue = 0, variable=self.unicode_mode)

        #Adding Menu to Bar
        #Προσθέτω τα δημιουργημένα Menu ως Submenu του Top-Level menu(menubar)
        menubar.add_cascade(menu=settings_menu, label="List Settings")
        menubar.add_cascade(menu=mode_menu, label = "Mode")

    """
        Μέθοδος που ορίζει την λίστα χαρακτήρων(self.list) κάνοντας Loop το list_settings και στην περίπτωση που
        είναι αληθές προσθέτη την αντίστοιχη λίστα στο self.list
    """
    def _manage_character_list(self):
        self.list = ""
        for index,x in enumerate(self.list_settings):
            if(x.get()):
                self.list += CHAR[index]

    """
        Μέθοδος Δημιουργίας ErrorBox
    """
    def _throw_error(self,text):
        tk.messagebox.showerror("Error", text)
    
    """
        Μέθοδος πιστοποίσης ορθότητας του Shift με την χρήση συνθικών και try-except δομή
        Άν επιστρέψει False τότε δεν τρέχει η μέθοδος κρυπτογράφισης και αποκρυπτογράφισης
    """
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

    """
        Διαδικασία κρυπτογράφισης
    """
    def encryption(self):
        encrypted = ""
        user_string = self.e1.get("1.0", "end-1c").strip() # Text to be encrypted
        shift = self.e2.get("1.0", 'end-1c').strip() # Remove all leading and ending whitespaces
        if(self._validate_shift(shift)): # Έλεγχος Shift

            """
                Κάνει Loop κάθε χαρακτήρα του user_string και προσθέτει στο encrypted
                το κωδικοποιημένο character. Άν είναι enabled το unicode_mode το if statement
                είναι ψευδές και άρα τρέχει το else. Όπου έιναι απλά κρυπτογράφιση του Καίσαρα με 
                με character List το Unicode μεχρι το U+FFFF Οπου καθιστά ένα αρκετά πύκνο υποσύνολο 
                του Unicode.
            """
            for i in user_string:
                if(not self.unicode_mode.get()):
                    index = self.list.find(i)
                    if(index == -1): # Αν δέν βρεθεί στην λίστα ο χαρακτήρας i
                        if(i in CHARACTERS_SKIP): #Ελέγχει την περίπτωση να είναι white-space ή \n αν είναι προσθέτει τον χαρακτήρα χωρις να τον αλλάξει αλλιώς επιστρέφει error και το αντικαταστεί με white-space
                            encrypted += i
                            continue
                        self._throw_error(f"Error: Symbol {i} couldn't found in the current character list, with unicode number {ord(i)}.\n Note: This character will be replaced with a whitespace.")
                        encrypted += " "
                        continue
                    encrypted += self.list[(index + int(shift)) % len(self.list)] # Περιορίζουμε το (index + int(shift)) αναμεσα στο 0 και το len(self.list) ωστε να μην έιναι out of bounds
                else:
                    encrypted += chr((ord(i) + int(shift)) % UNICODE_BOUND)
                
                # Κάνουμε Clear το TextBox του result και κάνουμε insert το κρυπτογραφιμένο text
                self.result.delete("1.0", tk.END)
                self.result.insert(tk.INSERT, encrypted)

    """
        Διαδικασία αποκρυπτογράφισης. Η διαδικασία ειναι παρόμοια με την διαδικασία της κρυπτογράφισης οπότε
        τα πολλά σχόλια είναι περιττά. Η μόνη διαφορα είναι οτι αντι να μετατοπίζεται προς την κατεύθυνση της κρυπτογράφισης
        ο χαρακτήρας μας μετατοπίζεται ως προς την αντίθετη κατεύθυνση επιστρέφοντας τον μη κρυπτογραφιμένο χαρακτήρα.
    """
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
                        decrypted += self.list[(index - int(shift)) % len(self.list)]
                    else:
                        decrypted += chr((ord(i) - int(shift)) % UNICODE_BOUND)
                    self.result.delete("1.0", tk.END)
                    self.result.insert(tk.INSERT, decrypted)

"""
Όταν καλεσθέι το πρόγραμμα καλέι την κλάση και έτσι τρέχει το πρόγραμμα
"""
if __name__ == "__main__":
    Graphics()