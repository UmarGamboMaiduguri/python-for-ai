# Stacks and Queues
# Author: Umar Gambo

from collections import deque


# Stack: Last In, First Out (LIFO)
stack = []

stack.append("Python")
stack.append("NumPy")
stack.append("Pandas")

print("--- Stack ---")
print("Stack:", stack)

removed_item = stack.pop()

print("Removed:", removed_item)
print("Stack after pop:", stack)


# Queue: First In, First Out (FIFO)
queue = deque()

queue.append("Student 1")
queue.append("Student 2")
queue.append("Student 3")

print("\n--- Queue ---")
print("Queue:", queue)

served_student = queue.popleft()

print("Served:", served_student)
print("Queue after serving:", queue)
