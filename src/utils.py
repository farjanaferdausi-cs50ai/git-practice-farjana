def total_passengers(data):
    return len(data)

def survival_count(data):
    return sum(p["Survived"] for p in data)