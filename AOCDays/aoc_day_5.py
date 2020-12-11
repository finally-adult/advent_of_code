import os


def solve_day_5():
	file = os.path.join("Assets", "aoc_day_5.txt")

	with open(file, "r") as file:
		data = file.read().splitlines()

	print("Case 1:")
	print("-------")
	solve_case_1(data)
	print("\nCase 2:")
	print("-------")
	solve_case_2(data)
	print("\n")


def solve_case_1(data):
	santa_list = SantaList(data)
	santa_list.parse_list_case_1()

	print(f"Nice kids: {santa_list.nice_count()}")


def solve_case_2(data):
	santa_list = SantaList(data)
	santa_list.parse_list_case_2()

	print(f"Nice kids: {santa_list.nice_count()}")


class SantaList:
	def __init__(self, santa_list):
		self.santa_list = santa_list
		self.checked_list = {}

	def naughty_count(self):
		count = 0
		for kid, nice in self.checked_list.items():
			if not nice:
				count += 1
		return count

	def nice_count(self):
		count = 0
		for kid, nice in self.checked_list.items():
			if nice:
				count += 1
		return count

	def parse_list_case_1(self):
		for kid in self.santa_list:
			check = Kid(kid)
			self.checked_list[kid] = check.is_nice_case_1()

	def parse_list_case_2(self):
		for kid in self.santa_list:
			check = Kid(kid)
			self.checked_list[kid] = check.is_nice_case_2()


class Kid:
	def __init__(self, kid):
		self.kid = kid

	def is_nice_case_1(self):
		for naughty_string in Constants.NAUGHTY_STRINGS:
			if naughty_string in self.kid:
				return False

		vowel_count = 0
		for vowel in Constants.VOWELS:
			for letter in self.kid:
				if vowel == letter:
					vowel_count += 1

		if vowel_count >= 3:
			for i in range(len(self.kid) - 1):
				if self.kid[i] == self.kid[i + 1]:
					return True
			return False

	def is_nice_case_2(self):
		return True


class Constants:
	VOWELS = ["a", "e", "i", "o", "u"]
	NAUGHTY_STRINGS = ["ab", "cd", "pq", "xy"]
