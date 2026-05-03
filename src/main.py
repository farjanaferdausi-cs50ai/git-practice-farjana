print("Farjana Ferdausi")
print("Titanic Data Analysis Project")

from utils import *

data = [
    {"Name": "Jack", "Sex": "male", "Pclass": 3, "Age": 20, "Survived": 0},
    {"Name": "Rose", "Sex": "female", "Pclass": 1, "Age": 19, "Survived": 1}
]

print("===== Titanic Data Analysis Report =====")

print(f"Total Passengers: {total_passengers(data)}")
print(f"Total Survived: {survival_count(data)}")
print(f"Overall Survival Rate: {survival_rate(data):.2f}%")

print(f"Female Survival Rate: {gender_survival_rate(data, 'female'):.2f}%")
print(f"Male Survival Rate: {gender_survival_rate(data, 'male'):.2f}%")

print(f"First Class Survival Rate: {class_survival_rate(data, 1):.2f}%")
print(f"Third Class Survival Rate: {class_survival_rate(data, 3):.2f}%")

print(f"Average Age: {average_age(data):.2f}")

print(f"Safe Survival Count: {safe_survival_count(data)}")


