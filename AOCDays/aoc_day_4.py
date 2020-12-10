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
	for i in range(10000000):
		advent_coin = hashlib.md5(f"{hash_input}{str(i)}".encode("utf-8")).hexdigest()
		if advent_coin[0:5] == "00000":
			print(advent_coin)
			print(f"{hash_input}{i}")
			break


def solve_case_two(hash_input):
	for i in range(10000000):
		advent_coin = hashlib.md5(f"{hash_input}{str(i)}".encode("utf-8")).hexdigest()
		if advent_coin[0:6] == "000000":
			print(advent_coin)
			print(f"{hash_input}{i}")
			break
