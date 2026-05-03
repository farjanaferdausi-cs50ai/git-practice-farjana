print("Farjana Ferdausi")
print("Titanic Data Analysis Project")

from utils import total_passengers, survival_count

data = [
    {"Name": "Jack", "Survived": 0},
    {"Name": "Rose", "Survived": 1}
]

print("Total:", total_passengers(data))
print("Survived:", survival_count(data))