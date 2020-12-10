import os


def solve_day_one():
	file = os.path.join("Assets", "aoc_day_one.txt")

	with open(file, "r") as file:
		directions = file.read()

	print("Case 1:")
	print("-------")
	solve_case_one(directions)
	print("\nCase 2:")
	print("-------")
	solve_case_two(directions)
	print("\n")


def solve_case_one(directions):
	count = 0

	for direction in directions:
		count = count + 1 if direction == "(" else count - 1

	print(f"Final floor: {count}")


def solve_case_two(directions):
	count = 0

	for index, direction in enumerate(directions):
		count = count + 1 if direction == "(" else count - 1
		if count == -1:
			print(f"Basement floor: {index + 1}")
			break
