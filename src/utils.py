def total_passengers(data):
    return len(data)

def survival_count(data):
    return sum(p["Survived"] for p in data)

def safe_survival_count(data):
    try:
        return sum(p["Survived"] for p in data)
    except:
        return 0

def gender_survival_rate(data, gender):
    group = [p for p in data if p.get("Sex") == gender]
    try:
        survived = sum(p["Survived"] for p in group)
        return (survived / len(group)) * 100
    except:
        return 0

def class_survival_rate(data, pclass):
    group = [p for p in data if p.get("Pclass") == pclass]
    try:
        survived = sum(p["Survived"] for p in group)
        return (survived / len(group)) * 100
    except:
        return 0

def average_age(data):
    ages = [p["Age"] for p in data if p.get("Age") is not None]
    try:
        return sum(ages) / len(ages)
    except:
        return 0

def safe_survival_count(data):
    try:
        return sum(p["Survived"] for p in data)
    except:
        return 0