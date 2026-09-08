# Python File Handling Practice
# Author: Umar Gambo

filename = "student_notes.txt"

# Write data to a file
with open(filename, "w") as file:
    file.write("Student: Umar Gambo\n")
    file.write("Subject: Computer Science\n")
    file.write("Topic: Python File Handling\n")

print("File created successfully.")

# Read data from the file
with open(filename, "r") as file:
    content = file.read()

print("\n--- File Contents ---")
print(content)
