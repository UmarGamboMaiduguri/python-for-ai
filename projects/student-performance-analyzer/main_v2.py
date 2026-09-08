# Student Performance Analyzer v2
# Author: Umar Gambo

def get_score(subject):
    while True:
        try:
            score = float(input(f"Enter {subject} score (0-100): "))

            if 0 <= score <= 100:
                return score

            print("Please enter a score between 0 and 100.")

        except ValueError:
            print("Please enter a valid number.")


name = input("Enter student name: ")

math = get_score("Math")
english = get_score("English")
computer = get_score("Computer Science")

total = math + english + computer
average = total / 3

if average >= 70:
    grade = "A"
elif average >= 60:
    grade = "B"
elif average >= 50:
    grade = "C"
elif average >= 45:
    grade = "D"
elif average >= 40:
    grade = "E"
    
else:
    grade = "F"

print("\n--- Student Performance Report ---")
print(f"Student: {name}")
print(f"Total Score: {total:.2f}")
print(f"Average Score: {average:.2f}")
print(f"Grade: {grade}")
