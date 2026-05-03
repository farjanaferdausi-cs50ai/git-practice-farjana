def total_passengers(data):
    return len(data)

def survival_count(data):
    return sum(p["Survived"] for p in data)

def safe_survival_count(data):
    try:
        return sum(p["Survived"] for p in data)
    except:
        return 0