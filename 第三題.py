# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 08:47:46 2024

@author: Student
"""

import random


questions_dict = {
    "What is the capital of France?": "Paris",
    "What is the largest planet in our solar system?": "Jupiter",
    "Who wrote 'To Kill a Mockingbird'?": "Harper Lee",
    "What element does 'O' represent on the periodic table?": "Oxygen",
    "In what year did the Titanic sink?": "1912"
}

num_selections = 3   
selected_questions = random.sample(list(questions_dict.items()), num_selections)

for question, answer in selected_questions:
    print(f"{question}: {answer}")
