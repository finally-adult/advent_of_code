

if __name__ == "__main__":
    while True:
        print("Advent of Code!")
        print("---------------")
        day_input = (input("Which day? 'q' to quit\n"))

        if day_input == "q":
            break

        try:
            module = __import__("AOCDays")
            func = getattr(module, f"solve_day_{str(day_input)}")
            func()
        except AttributeError:
            try:
                if int(day_input) <= 25:
                    print(f"Day {day_input} does not exist yet!\n")
                else:
                    print("Advent of Code only goes up to Christmas!\n")
            except ValueError:
                print("Please input a valid number or 'q'\n")

