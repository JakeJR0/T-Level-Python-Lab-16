import tkinter

import pandas as pd
from datetime import datetime
import re

user_information = pd.read_csv("program_data/user_information.csv")  # Initialises the Variable


def load_user_information():
    global user_information
    try:
        user_information = pd.read_csv("program_data/user_information.csv")  # Updates the Variable
    except:
        pass


def save_user_information():
    global user_information
    try:
        user_information.to_csv("program_data/user_information.csv")  # Saves the Variable
    except:
        pass


def valid_length(item="", max_len=0):
    try:
        if len(item) <= max_len:  # Checks if the length of the string is within the correct range
            return True
        else:
            return False
    except:
        return False


def valid_postcode(postcode=""):
    if len(postcode) == 6 or 7:  # Checks if the length of the postcode is within the range
        return True
    return False


def valid_age(age=0):
    try:
        if age > 18:  # Checks if the age is greater than 18
            if age < 75:  # Checks if the age is less than 75
                return True
            else:
                return False
        else:
            return False
    except:
        return False


def valid_birthday(birthday=""):
    try:
        datetime.strptime(birthday, "%d/%m/%Y")  # Checks if the data can be converted without breaking.
        return True
    except:
        return False


def valid_email(email=""):
    valid = False
    at_matches = re.findall("@", email)  # Gets all @'s within the string
    dot_matches = re.findall(".", email)  # Gets all .'s within the string

    if len(at_matches) > 0:
        valid = True

    if len(dot_matches) <= 0:
        if valid:  # Checks if it is valid
            valid = False  # Changes the value

    return valid


class App():
    show_frames = []
    show_entries = []

    def show_frame(self, frame=None):
        for i in self.show_frames:
            if frame != i:
                i.pack_forget()
            else:
                i.pack()

    def focus_entry(self, entry):
        for i in self.show_entries:
            if entry == i:
                entry.focus()

    def show_clear_result(self, event=None):
        self.show_entry_result.config(text="")

    def show_submit(self, event=None):
        first_name = self.show_entry_fn.get()
        last_name = self.show_entry_ln.get()
        email = self.show_entry_email.get()
        street_address = self.show_entry_sa.get()
        district_address = self.show_entry_da.get()
        town_address = self.show_entry_ta.get()
        country_address = self.show_entry_ca.get()
        postcode = self.show_entry_postcode.get()
        birthday = self.show_entry_birthday.get()
        age = self.show_entry_age.get()

        if valid_email(email):
            print("Valid Email")
        else:
            self.show_entry_result.config(text="Invalid Email.")
            self.show_entry_result.after(500, self.show_clear_result)
            return

        if valid_postcode(postcode):
            print("Valid Postcode")
        else:
            self.show_entry_result.config(text="Invalid Postcode.")
            self.show_entry_result.after(500, self.show_clear_result)
            return

        if valid_length(first_name, 10):
            print("Valid First Name")
        else:
            self.show_entry_result.config(text="Invalid First Name.")
            self.show_entry_result.after(500, self.show_clear_result)
            return

        if valid_age(age):
            print("Valid Age")
        else:
            self.show_entry_result.config(text="Invalid Age.")
            self.show_entry_result.after(500, self.show_clear_result)
            return

        if valid_birthday(birthday):
            print("Valid Birthday")
        else:
            self.show_entry_result.config(text="Invalid Birthday.")
            self.show_entry_result.after(500, self.show_clear_result)
            return

        if valid_length(last_name, 20):
            print("Valid Last Name")
        else:
            self.show_entry_result.config(text="Invalid Last Name.")
            self.show_entry_result.after(500, self.show_clear_result)
            return

        if valid_length(street_address, 20):
            print("Valid Street Address")
        else:
            self.show_entry_result.config(text="Invalid Street Address.")
            self.show_entry_result.after(500, self.show_clear_result)
            return

        if valid_length(district_address, 20):
            print("Valid District Address")
        else:
            self.show_entry_result.config(text="Invalid District Address.")
            self.show_entry_result.after(500, self.show_clear_result)
            return

        if valid_length(town_address, 20):
            print("Valid Town")
        else:
            self.show_entry_result.config(text="Invalid Town Address.")
            self.show_entry_result.after(500, self.show_clear_result)
            return

        if valid_length(country_address, 20):
            print("Valid Country")
        else:
            self.show_entry_result.config(text="Invalid Country.")
            self.show_entry_result.after(500, self.show_clear_result)
            return

        # If here they have passed verification
        self.show_clear_form()  # Clears the form

    def show_clear_form(self):
        self.show_entry_fn.delete(0, tkinter.END)
        self.show_entry_ln.delete(0, tkinter.END)
        self.show_entry_email.delete(0, tkinter.END)
        self.show_entry_sa.delete(0, tkinter.END)
        self.show_entry_da.delete(0, tkinter.END)
        self.show_entry_ta.delete(0, tkinter.END)
        self.show_entry_ca.delete(0, tkinter.END)
        self.show_entry_postcode.delete(0, tkinter.END)
        self.show_entry_birthday.delete(0, tkinter.END)
        self.show_entry_age.delete(0, tkinter.END)

    def set_focus_ln(self, event=None):  # Sets the focus to the next entry
        self.show_entry_ln.focus()

    def set_focus_email(self, event=None):  # Sets the focus to the next entry
        self.show_entry_email.focus()

    def set_focus_sa(self, event=None):  # Sets the focus to the next entry
        self.show_entry_sa.focus()

    def set_focus_da(self, event=None):  # Sets the focus to the next entry
        self.show_entry_da.focus()

    def set_focus_town(self, event=None):  # Sets the focus to the next entry
        self.show_entry_ta.focus()

    def set_focus_country(self, event=None):  # Sets the focus to the next entry
        self.show_entry_ca.focus()

    def set_focus_postcode(self, event=None):  # Sets the focus to the next entry
        self.show_entry_postcode.focus()

    def set_focus_birthday(self, event=None):  # Sets the focus to the next entry
        self.show_entry_birthday.focus()

    def set_focus_age(self, event=None):  # Sets the focus to the next entry
        self.show_entry_age.focus()

    def __init__(self):
        self.root = tkinter.Tk()  # Creates an app
        self.root.geometry("800x300")  # Sets the app size
        self.root.title("Python Lab 16")  # Sets the app title

        self.main_menu = tkinter.Menu(self.root, tearoff=0)  # Creates a menu
        self.select_menu = tkinter.Menu(self.main_menu, tearoff=0) # Creates a sub menu
        self.select_menu.add_command(label="Add Data", command=lambda: self.show_frame(self.entry_screen))
        self.main_menu.add_cascade(label="Select", menu=self.select_menu)
        self.main_menu.add_command(label="Exit Program", command=lambda: self.root.destroy())
        self.root.config(menu=self.main_menu)

        self.entry_screen = tkinter.Frame(self.root) # Creates a frame
        self.entry_screen.pack() # Packs the screen

        self.show_frame(frame=self.entry_screen)
        self.show_title = tkinter.Label(self.entry_screen, text="User Information", font=("Arial", 24))

        self.show_submit_button = tkinter.Button(self.entry_screen, text="Submit",
                                                 command=self.show_submit)  # Creates a Label widget
        self.show_entry_fn_label = tkinter.Label(self.entry_screen, text="First Name:",
                                                 font=("Arial", 12))  # Creates a Label widget
        self.show_entry_ln_label = tkinter.Label(self.entry_screen, text="Last Name:",
                                                 font=("Arial", 12))  # Creates a Label widget
        self.show_entry_email_label = tkinter.Label(self.entry_screen, text="Email: ",
                                                    font=("Arial", 12))  # Creates a Label widget
        self.show_entry_sa_label = tkinter.Label(self.entry_screen, text="Street Address:",
                                                 font=("Arial", 12))  # Creates a Label widget
        self.show_entry_da_label = tkinter.Label(self.entry_screen, text="District Address:",
                                                 font=("Arial", 12))  # Creates a Label widget
        self.show_entry_ta_label = tkinter.Label(self.entry_screen, text="Town:",
                                                 font=("Arial", 12))  # Creates a Label widget
        self.show_entry_ca_label = tkinter.Label(self.entry_screen, text="Country",
                                                 font=("Arial", 12))  # Creates a Label widget
        self.show_entry_postcode_label = tkinter.Label(self.entry_screen, text="Postcode:",
                                                       font=("Arial", 12))  # Creates a Label widget
        self.show_entry_birthday_label = tkinter.Label(self.entry_screen, text="Birthday (DD/MM/YY)",
                                                       font=("Arial", 12))  # Creates a Label widget
        self.show_entry_age_label = tkinter.Label(self.entry_screen, text="Age",
                                                  font=("Arial", 12))  # Creates a Label widget
        self.show_entry_result = tkinter.Label(self.entry_screen, text="", font=("Arial", 12))  # Creates a Label widget

        self.show_entry_fn = tkinter.Entry(self.entry_screen)  # Creates an entry widget
        self.show_entry_ln = tkinter.Entry(self.entry_screen)  # Creates an entry widget
        self.show_entry_email = tkinter.Entry(self.entry_screen)  # Creates an entry widget
        self.show_entry_sa = tkinter.Entry(self.entry_screen)  # Creates an entry widget
        self.show_entry_da = tkinter.Entry(self.entry_screen)  # Creates an entry widget
        self.show_entry_ta = tkinter.Entry(self.entry_screen)  # Creates an entry widget
        self.show_entry_ca = tkinter.Entry(self.entry_screen)  # Creates an entry widget
        self.show_entry_postcode = tkinter.Entry(self.entry_screen)  # Creates an entry widget
        self.show_entry_birthday = tkinter.Entry(self.entry_screen)  # Creates an entry widget
        self.show_entry_age = tkinter.Entry(self.entry_screen)  # Creates an entry widget

        self.show_title.grid(row=1, column=1, columnspan=3)  # Positions the widget.
        self.show_entry_fn_label.grid(row=3, column=1)  # Positions the widget.
        self.show_entry_ln_label.grid(row=4, column=1)  # Positions the widget.
        self.show_entry_email_label.grid(row=5, column=1)  # Positions the widget.
        self.show_entry_sa_label.grid(row=6, column=1)  # Positions the widget.
        self.show_entry_da_label.grid(row=7, column=1)  # Positions the widget.
        self.show_entry_ta_label.grid(row=8, column=1)  # Positions the widget.
        self.show_entry_ca_label.grid(row=9, column=1)  # Positions the widget.
        self.show_entry_postcode_label.grid(row=10, column=1)  # Positions the widget.
        self.show_entry_birthday_label.grid(row=11, column=1)  # Positions the widget.
        self.show_entry_age_label.grid(row=12, column=1)  # Positions the widget.
        self.show_entry_fn.grid(row=3, column=2)  # Positions the widget.
        self.show_entry_ln.grid(row=4, column=2)  # Positions the widget.
        self.show_entry_email.grid(row=5, column=2)  # Positions the widget.
        self.show_entry_sa.grid(row=6, column=2)  # Positions the widget.
        self.show_entry_da.grid(row=7, column=2)  # Positions the widget.
        self.show_entry_ta.grid(row=8, column=2)  # Positions the widget.
        self.show_entry_ca.grid(row=9, column=2)  # Positions the widget.
        self.show_entry_postcode.grid(row=10, column=2)  # Positions the widget.
        self.show_entry_birthday.grid(row=11, column=2)  # Positions the widget.
        self.show_entry_age.grid(row=12, column=2)  # Positions the widget.
        self.show_entry_result.grid(row=13, column=1, columnspan=3)  # Positions the widget.
        self.show_submit_button.grid(row=14, column=2)  # Positions the widget.

        self.show_entry_fn.bind("<Return>", self.set_focus_ln)  # Binds the return key.
        self.show_entry_ln.bind("<Return>", self.set_focus_email)  # Binds the return key.
        self.show_entry_email.bind("<Return>", self.set_focus_sa)  # Binds the return key.
        self.show_entry_sa.bind("<Return>", self.set_focus_da)  # Binds the return key.
        self.show_entry_da.bind("<Return>", self.set_focus_town)  # Binds the return key.
        self.show_entry_ta.bind("<Return>", self.set_focus_country)  # Binds the return key.
        self.show_entry_ca.bind("<Return>", self.set_focus_postcode)  # Binds the return key.
        self.show_entry_postcode.bind("<Return>", self.set_focus_birthday)  # Binds the return key.
        self.show_entry_birthday.bind("<Return>", self.set_focus_age)  # Binds the return key.
        self.show_entry_age.bind("<Return>", self.show_submit)  # Binds the return key.

        self.root.mainloop()


App()
