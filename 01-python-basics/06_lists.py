# Python Lists Practice
# Author: Umar Gambo

scores = [85, 72, 65, 90, 78]

print("--- Student Scores ---")
print(scores)

print("\nFirst score:", scores[0])
print("Last score:", scores[-1])

print("\nTotal students:", len(scores))

print("\nSorted scores:")
print(sorted(scores))

print("\nHighest score:", max(scores))
print("Lowest score:", min(scores))

average = sum(scores) / len(scores)
print("Average score:", average)
