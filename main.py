import random

"""
array = [
        ['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']
        ]

for x in range(len(array[0])):
    for y in range(len(array)):
        print(array[y][x], end="")
    print("\n")

"""

userint = input("Make a selection(0/1)")
randint = random.randint(0, 1)
print(randint)
if userint == randint:
    print("You won!")
else:
    print("The computer won.")