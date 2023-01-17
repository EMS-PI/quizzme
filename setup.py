"""ui.py: Setup for QuizMe App

A simple trivia app based on the code found in the credits.
Uses Open Trivia Database (https://opentdb.com/) as the source
of questions."""

import tkinter as tk

__author__ = "Ethem M Sözer"
__copyright__ = "Copyright 2023, EMS_PI"
__credits__ = ["100 Days of Code: The Complete Python Pro Bootcamp for 2023 - Dr. Angela Yu"]
__license__ = "MIT"

THEME_COLOR = "#375362"

CATEGORIES = [
    "Any category",
    "Science & Nature",
    "Science: Computers",
    "Science: Mathematics",
    "Mythology",
    "Geography",
    "History",
    "Politics",
    "Animals",
    "Vehicles"
]

CATEGORY_IDS = [
    0,
    17,
    18,
    19,
    20,
    22,
    23,
    24,
    27,
    28
]

DIFFICULTY_LEVELS = [
    "Any difficulty",
    "Easy",
    "Medium",
    "Hard"
]


class SetupUI:
    def __init__(self, main_ui, selected_params):
        self.main_ui = main_ui

        self.window = tk.Toplevel()
        self.window.title("QuizMe: Setup")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        category_label = tk.Label(self.window, text="Category:", anchor='e', justify='left',
                                  bg=THEME_COLOR, fg="white")
        category_label.grid(row=0, column=0)
        self.category = tk.StringVar()
        self.category.set(CATEGORIES[CATEGORY_IDS.index(selected_params["category"])])
        self.category_dropdown = tk.OptionMenu(self.window, self.category, *CATEGORIES)
        self.category_dropdown.config(width=20, bg=THEME_COLOR, fg="white", highlightthickness=0)
        self.category_dropdown.grid(row=0, column=1)

        difficulty_label = tk.Label(self.window, text="Difficulty:", anchor='e',
                                    justify='left', bg=THEME_COLOR, fg="white")
        difficulty_label.grid(row=1, column=0)
        self.difficulty = tk.StringVar()
        self.difficulty.set(selected_params["difficulty"].capitalize())
        self.difficulty_dropdown = tk.OptionMenu(self.window, self.difficulty, *DIFFICULTY_LEVELS)
        self.difficulty_dropdown.config(width=20, bg=THEME_COLOR, fg="white", highlightthickness=0)
        self.difficulty_dropdown.grid(row=1, column=1)

        num_questions_label = tk.Label(self.window, text="Number of questions:", anchor='e',
                                       justify='left', bg=THEME_COLOR, fg="white")
        num_questions_label.grid(row=2, column=0)
        self.num_questions_edit = tk.Entry(self.window)
        self.num_questions_edit.config(width=26, bg=THEME_COLOR, fg="white")
        self.num_questions_edit.insert(0, selected_params["num_questions"])
        self.num_questions_edit.grid(row=2, column=1)

        self.ok_button = tk.Button(self.window, text="OK", command=self.pass_selections)
        self.ok_button.config(width=22, bg=THEME_COLOR, fg="white")
        self.ok_button.grid(row=3, column=1)

        self.window.mainloop()

    def pass_selections(self):
        category = self.category.get()
        category_id = CATEGORY_IDS[CATEGORIES.index(category)]
        difficulty = self.difficulty.get()
        num_questions = self.num_questions_edit.get()

        self.main_ui.setup_quiz(category_id, difficulty, num_questions)
        self.window.destroy()
