import inflect


if __name__ == "__main__":
    while True:
        p = inflect.engine()
        print("Advent of Code!")
        print("---------------")
        day_input_int = (input("Which day? 'q' to quit\n"))

        if day_input_int == "q":
            break

        day_input = p.number_to_words(day_input_int)

        try:
            module = __import__("AOCDays")
            func = getattr(module, f"solve_day_{day_input}")
            func()
        except AttributeError:
            if day_input == "zero":
                print("Please enter a valid number\n")
            elif int(day_input_int) <= 25:
                print(f"Day {day_input_int} does not exist yet!\n")
            else:
                print("Advent of Code only goes up to Christmas!\n")
