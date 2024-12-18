import random


def get_user_numbers():
    numbers = []
    while len(numbers) < 6:
        try:
            user_input = input(f"Enter number {len(numbers) + 1} (1-49): ")
            number = int(user_input)
            if number < 1 or number > 49:
                print("Please enter a number between 1 and 49.")
            elif number in numbers:
                print("You've already entered that number. Please choose another.")
            else:
                numbers.append(number)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    numbers.sort()
    return numbers


def draw_lotto_numbers():
    return sorted(random.sample(range(1, 50), 6))


def main():
    print("Welcome to the LOTTO Simulator!")

    user_numbers = get_user_numbers()
    print(f"Your selected numbers are: {user_numbers}")

    drawn_numbers = draw_lotto_numbers()
    print(f"The drawn numbers are: {drawn_numbers}")

    matching_numbers = set(user_numbers) & set(drawn_numbers)
    num_matches = len(matching_numbers)

    print(f"You matched {num_matches} numbers: {sorted(matching_numbers)}")

    if num_matches == 6:
        print("Congratulations! You have won the jackpot!")
    else:
        print("Better luck next time!")


if __name__ == "__main__":
    main()
