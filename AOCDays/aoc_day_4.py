import os
import hashlib


def solve_day_4():
	file = os.path.join("Assets", "aoc_day_4.txt")

	with open(file, "r") as file:
		hash_input = file.read()

	print("Case 1:")
	print("-------")
	solve_case_one(hash_input)
	print("\nCase 2:")
	print("-------")
	solve_case_two(hash_input)
	print("\n")


def solve_case_one(hash_input):
	i = 0
	while not hashlib.md5(f"{hash_input}{str(i)}".encode("utf-8")).hexdigest().startswith("00000"):
		i += 1

	print(f"{str(i)} makes hash: {hashlib.md5(f'{hash_input}{str(i)}'.encode('utf-8')).hexdigest()}")


def solve_case_two(hash_input):
	i = 0
	while not hashlib.md5(f"{hash_input}{str(i)}".encode("utf-8")).hexdigest().startswith("000000"):
		i += 1

	print(f"{str(i)} makes hash: {hashlib.md5(f'{hash_input}{str(i)}'.encode('utf-8')).hexdigest()}")
