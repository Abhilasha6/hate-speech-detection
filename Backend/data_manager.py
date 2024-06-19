# data_manager.py

import json
import os

# Define the initial users_data
users_data = {
    "users": [
        {
            "username": "abhinav",
            "monthlyData": {
                "January": [
                    [88, 76, 30, 75, 65, 26],
                    [94, 70, 70, 97, 0, 71],
                    [94, 70, 70, 97, 0, 71],
                    [94, 70, 70, 97, 0, 71],
                    [6, 14, 45, 5, 2, 7],
                    [0, 0, 0, 0, 0, 0]
                ],
                "February": [
                    [88, 80, 82, 34, 76, 5],
                    [94, 70, 70, 97, 0, 71],
                    [33, 89, 77, 85, 12, 21]
                ],
                "March": [
                    [13, 58, 5, 68, 86, 88],
                    [94, 70, 70, 97, 0, 71],
                    [5, 86, 9, 38, 86, 79],
                    [0, 0, 0, 0, 0, 0]
                ],
                "April": [
                    [8, 46, 58, 1, 4, 24],
                    [94, 70, 70, 97, 0, 71],
                    [24, 48, 50, 9, 99, 29]
                ],
                "May": [
                    [59, 78, 52, 54, 32, 90],
                    [94, 70, 70, 97, 0, 71],
                    [94, 70, 70, 97, 0, 71],
                    [94, 70, 70, 97, 0, 71],
                    [75, 47, 2, 86, 97, 88]
                ]
            }
        },
        {
            "username": "sunil",
            "monthlyData": {
                "January": [
                    [88, 76, 30, 75, 65, 26],
                    [94, 70, 70, 97, 0, 71],
                    [94, 70, 70, 97, 0, 71],
                    [6, 14, 45, 5, 2, 7]
                ],
                "February": [
                    [88, 80, 82, 34, 76, 5],
                    [94, 70, 70, 97, 0, 71]
                ],
                "March": [
                    [94, 70, 70, 97, 0, 71],
                    [5, 86, 9, 38, 86, 79]
                ],
                "April": [
                    [94, 70, 70, 97, 0, 71],
                    [24, 48, 50, 9, 99, 29]
                ],
                "May": [
                    [94, 70, 70, 97, 0, 71],
                    [94, 70, 70, 97, 0, 71],
                    [94, 70, 70, 97, 0, 71],
                    [75, 47, 2, 86, 97, 88]
                ]
            }
        },
        {
            "username": "rohini",
            "monthlyData": {
                "January": [
                    [94, 70, 70, 97, 0, 71],
                    [94, 70, 70, 97, 0, 71],
                    [94, 70, 70, 97, 0, 71],
                    [6, 14, 45, 5, 2, 7]
                ],
                "February": [
                    [88, 80, 82, 34, 76, 5],
                    [33, 89, 77, 85, 12, 21]
                ],
                "March": [
                    [13, 58, 5, 68, 86, 88],
                    [94, 70, 70, 97, 0, 71]
                ],
                "April": [
                    [94, 70, 70, 97, 0, 71],
                    [24, 48, 50, 9, 99, 29]
                ],
                "May": [
                    [59, 78, 52, 54, 32, 90],
                    [94, 70, 70, 97, 0, 71],
                    [75, 47, 2, 86, 97, 88]
                ]
            }
        }
    ]
}

data_file = 'users_data.json'

def load_users_data():
    global users_data
    if os.path.exists(data_file):
        with open(data_file, 'r') as file:
            users_data = json.load(file)

def save_users_data():
    with open(data_file, 'w') as file:
        json.dump(users_data, file, indent=4)

# Load initial data
load_users_data()
