# Student Performance Analyzer
# Author: Umar Gambo

name = input("Enter student name: ")

math = float(input("Enter Math score: "))
english = float(input("Enter English score: "))
computer = float(input("Enter Computer Science score: "))

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
print(f"Grade: {grade}")0

