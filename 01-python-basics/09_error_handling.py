# Python Error Handling Practice
# Author: Umar Gambo

while True:
    try:
        score = float(input("Enter a score (0-100): "))

        if 0 <= score <= 100:
            print("Valid score:", score)
            break

        print("Error: Score must be between 0 and 100.")

    except ValueError:
        print("Error: Please enter a valid number.")
