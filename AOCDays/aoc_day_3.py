import os


def solve_day_3():
    file = os.path.join("Assets", "aoc_day_3.txt")

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
    santa = RealSanta(directions)

    santa.deliver()

    print(f"Santa unique houses: {santa.unique_house_count()}")


def solve_case_two(directions):
    santa = RealSanta(directions)
    robo_santa = RoboSanta(directions)

    santa.deliver_with_help()
    robo_santa.help_santa_deliver()

    all_houses = santa.houses_visited + robo_santa.houses_visited
    all_houses_set = list(set(tuple(house) for house in all_houses))

    print(f"Number of Santa houses: {santa.unique_house_count()}")
    print(f"Number of Robo-Santa house: {robo_santa.unique_house_count()}")
    print(f"Total Houses: {len(all_houses_set)}")


class Santa:
    def __init__(self, directions):
        self.directions = directions
        self.start = [0, 0]
        self.houses_visited = []

    def move(self, direction):
        if direction == ">":
            self.start[1] += 1
        elif direction == "^":
            self.start[0] += 1
        elif direction == "<":
            self.start[1] -= 1
        else:
            self.start[0] -= 1
        self.visit_house([house for house in self.start])

    def visit_house(self, house):
        self.houses_visited.append(house)

    def unique_house_count(self):
        return len(list(set(tuple(house) for house in self.houses_visited)))


class RoboSanta(Santa):
    def __init__(self, directions):
        super().__init__(directions)

    def help_santa_deliver(self):
        for index, house in enumerate(self.directions):
            if index % 2:
                self.move(house)


class RealSanta(Santa):
    def __init__(self, directions):
        super().__init__(directions)

    def deliver(self):
        for house in self.directions:
            self.move(house)

    def deliver_with_help(self):
        for index, house in enumerate(self.directions):
            if not index % 2:
                self.move(house)
