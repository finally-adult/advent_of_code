import os


def solve_day_2():
    file = os.path.join("Assets", "aoc_day_2.txt")

    with open(file, "r") as file:
        data = file.readlines()

    sizes_list = []

    for line in data:
        sizes_list.append(line.split("x"))

    present_list = [Present(int(size[0]), int(size[1]), int(size[2])) for size in sizes_list]

    print("Case 1:")
    print("-------")
    solve_case_one(present_list)
    print("\nCase 2:")
    print("-------")
    solve_case_two(present_list)
    print("\n")


def solve_case_one(presents):
    total_amount_of_paper = 0

    for present in presents:
        total_amount_of_paper += present.amount_of_paper()

    print(f"Total amount of paper: {total_amount_of_paper}")


def solve_case_two(presents):
    total_amount_of_ribbon = 0

    for present in presents:
        total_amount_of_ribbon += present.amount_of_ribbon()

    print(f"Total amount of ribbon: {total_amount_of_ribbon}")


class Present:
    def __init__(self, height, length, width):
        self.height = height
        self.length = length
        self.width = width

    def area_of_smallest_side(self):
        return min(self.height * self.length, self.height * self.width, self.width * self.length)

    def total_area(self):
        return (2*self.length*self.width) + (2*self.width*self.height) + (2*self.height*self.length)

    def amount_of_paper(self):
        return self.total_area() + self.area_of_smallest_side()

    def ribbon_for_bow(self):
        return self.height * self.width * self.length

    def ribbon_for_box(self):
        smallest_two = [self.height, self.width, self.length]
        smallest_two.sort()
        return (2*smallest_two[0]) + (2*smallest_two[1])

    def amount_of_ribbon(self):
        return self.ribbon_for_bow() + self.ribbon_for_box()
