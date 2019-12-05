"""
All versions of foods.py in this section have avoided using for loops when printing to save space. Choose a version of foods.py, and write two for loops to print each list of foods.
"""

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('Ini')
friend_foods.append('Itu')

print("My favorite foods are:")
for food in my_foods:
	print(f"- {food.title()}")

print("\nMy friend's favorite foods are:")
for food in friend_foods:
	print(f"- {food.title()}")