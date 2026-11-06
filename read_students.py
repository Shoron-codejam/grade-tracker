import csv

def check_greade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "Fail"

with open("students.csv","r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        name = row["name"]
        score = int(row["score"])
        grade = check_greade(score)
        print(f'{name}: {score} -> {grade}')