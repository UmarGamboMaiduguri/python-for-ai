# Python Functions Practice
# Author: Umar Gambo


def calculate_average(scores):
    return sum(scores) / len(scores)


def calculate_grade(average):
    if average >= 70:
        return "A"
    elif average >= 60:
        return "B"
    elif average >= 50:
        return "C"
    elif average >= 45:
        return "D"
    elif average >= 40:
        return "E"
    else:
        return "F"


scores = [85, 78, 92]

average = calculate_average(scores)
grade = calculate_grade(average)

print("Scores:", scores)
print("Average:", round(average, 2))
print("Grade:", grade)
