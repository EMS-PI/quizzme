"""data.py: Data source for QuizMe App

A simple trivia app based on the code found in the credits.
Uses Open Trivia Database (https://opentdb.com/) as the source
of questions."""

import requests
from question_model import Question

__author__ = "Ethem M Sözer"
__copyright__ = "Copyright 2023, EMS_PI"
__credits__ = ["100 Days of Code: The Complete Python Pro Bootcamp for 2023 - Dr. Angela Yu"]
__license__ = "MIT"

QUIZ_DATA_SITE = 'https://opentdb.com/api.php'


def quiz_data(amount, category, difficulty):
    parameters = {
        "amount": int(amount),
        "category": category,
        "difficulty": difficulty.lower(),
        "type": "boolean"
    }
    if category == 0:
        del parameters["category"]
    if difficulty.lower() == "any difficulty":
        del parameters["difficulty"]
    question_response = requests.get(QUIZ_DATA_SITE, params=parameters)
    question_response.raise_for_status()
    temp = question_response.json()
    question_data = temp["results"]
    question_bank = []
    for q in question_data:
        question_bank.append(Question(q["question"], q["correct_answer"]))
    return question_bank
