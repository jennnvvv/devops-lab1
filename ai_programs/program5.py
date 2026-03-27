# Vacuum Cleaner Agent (4x4 Room)
import random

def display(room):
    for row in room:
        print(row)

room = [[1,1,1,1] for _ in range(4)]

print("All the rooms are dirty")
display(room)

# Random dirt
for i in range(4):
    for j in range(4):
        room[i][j] = random.choice([0,1])

print("\nBefore cleaning:")
display(room)

cleaned = 0

for i in range(4):
    for j in range(4):
        if room[i][j] == 1:
            print(f"Cleaning position: {i},{j}")
            room[i][j] = 0
            cleaned += 1

performance = 100 - ((cleaned / 16) * 100)

print("\nAfter cleaning:")
display(room)
print("Performance =", performance, "%")