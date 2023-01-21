from tkinter import *
from data import SCALES, MUSIC_NOTES


class Interface:

    def __init__(self):
        self.notes_list = []
        self.notes_numbs = []
        self.notes = ""
        self.scale_formula = []
        self.scale_names = ''.join(f"{key}\n" for key in SCALES.keys())
        self.window = Tk()
        self.window.title("Scale Finder")
        self.window.config(padx=20, pady=20)

        self.label = Label(text="Please enter five to twelve notes beginning with the tonal center:")
        self.label.grid(row=0, column=1)

        self.label2 = Label(text="Related Scales:")
        self.label2.grid(row=3, column=1)

        self.label_scales = Label(text=self.scale_names)
        self.label_scales.grid(row=4, column=1, rowspan=5)

        self.var = StringVar()
        self.user_input = Entry(self.window, textvariable=self.var)
        self.user_input.focus()
        self.user_input.config(width=50)
        self.user_input.grid(row=1, column=0, columnspan=2)

        # self.enter_button = Button(text="Enter", command=self.notes_to_nums)
        # self.enter_button.grid(row=1, column=2)

        self.scale_label = Label(text=" ")
        self.scale_label.grid(row=2, column=1)

        self.var.trace('w', self.user_entry)

        self.window.mainloop()

    def user_entry(self, *args):
        self.notes = self.var.get().upper().replace(",", " ")
        self.notes_list = [x.strip() for x in self.notes.split(' ')]
        self.notes_list = self.check_notes(self.notes_list)
        # if 5 > len(self.notes_list) > 12:
        #     self.scale_label.config(text="The scale must contain 5-12 notes.")
        # elif 5 <= len(self.notes_list) <= 12:
        #     self.scale_label.config(text=f"Great, this scale has {len(self.notes_list)} notes.")
        self.notes_to_nums()

    def notes_to_nums(self):
        """Converts str inputs from user into corresponding int in data"""
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
        self.scale_finder()

    def scale_finder(self):
        """Compares user scale formula with all scale formulas in data file. Returns type of scale to UI"""
        possible_scales = list(SCALES.keys())
        if len(self.scale_formula) <= 1:
            self.label_scales.config(text=''.join(f"{key}\n" for key in SCALES.keys()))
        else:
            for formula in SCALES.values():
                # print(formula)
                for x in range(0, len(self.scale_formula) - 1):
                    if formula[x] == self.scale_formula[x]:
                        pass
                    else:
                        possible_scales.remove((list(SCALES.keys())[list(SCALES.values()).index(formula)]))
                        break
        self.label_scales.config(text=''.join(f"{key}\n" for key in possible_scales))
