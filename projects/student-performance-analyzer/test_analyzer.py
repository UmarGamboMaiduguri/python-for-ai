# Tests for Student Performance Analyzer
# Author: Umar Gambo

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


# Test cases
assert calculate_grade(85) == "A"
assert calculate_grade(65) == "B"
assert calculate_grade(55) == "C"
assert calculate_grade(47) == "D"
assert calculate_grade(40) == "E"
assert calculate_grade(30) == "F"

print("All tests passed successfully!")
