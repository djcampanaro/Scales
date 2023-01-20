from tkinter import *
from data import SCALES, MUSIC_NOTES


class Interface:

    def __init__(self):
        self.notes_list = []
        self.notes_numbs = []
        self.notes = ""
        self.scale_formula = []
        self.window = Tk()
        self.window.title("Scale Finder")
        self.window.config(padx=20, pady=20)

        self.label = Label(text="Please enter five to seven notes beginning with the tonal center:")
        self.label.grid(row=0, column=1)

        self.user_input = Entry()
        self.user_input.focus()
        self.user_input.config(width=50)
        self.user_input.grid(row=1, column=0, columnspan=2)

        self.enter_button = Button(text="Enter", command=self.notes_to_nums)
        self.enter_button.grid(row=1, column=2)

        self.scale_label = Label(text=" ")
        self.scale_label.grid(row=2, column=1)

        self.window.mainloop()

    def notes_to_nums(self):
        """Converts str inputs from user into corresponding int in data"""
        self.notes = self.user_input.get().upper().replace(",", " ")
        self.notes_list = [x.strip() for x in self.notes.split(' ')]
        self.notes_list = self.check_notes(self.notes_list)

        self.notes_numbs = [MUSIC_NOTES[x] for x in self.notes_list]
        self.notes_numbs.append(self.notes_numbs[0])
        self.create_scale_formula(self.notes_numbs)

    def check_notes(self, notes_list):
        """Takes list of user inputs and checks to make sure they contain only musical notes"""
        n = 0
        not_notes = []
        for num in range(0, len(notes_list)):
            if notes_list[n] == '':
                notes_list.remove(notes_list[n])
            elif notes_list[n] in MUSIC_NOTES:
                n += 1
            else:
                not_notes.append(notes_list[n])
                notes_list.remove(notes_list[n])
        string_not_notes = ", ".join(not_notes)
        if len(not_notes) > 1:
            self.scale_label.config(text=f"Sorry, {string_not_notes} are not notes.")
        elif len(not_notes) == 1:
            self.scale_label.config(text=f"Sorry, {string_not_notes} is not a note.")
        return notes_list

    def create_scale_formula(self, notes_numbs):
        """Uses user int to find the spacing between notes, creating a scale formula"""
        for num in range(0, len(notes_numbs) - 1):
            if notes_numbs[num] > notes_numbs[num + 1]:
                notes_numbs[num + 1] += 12

        self.scale_formula = [notes_numbs[x + 1] - notes_numbs[x] for x in range(len(notes_numbs) - 1)]
        self.scale_finder(self.scale_formula)

    def scale_finder(self, scale_formula):
        """Compares user scale formula with all scale formulas in data file. Returns type of scale to UI"""
        for x in SCALES.values():
            if x == scale_formula:
                scale = (list(SCALES.keys())[list(SCALES.values()).index(x)])
                self.scale_label.config(text=scale)
