import random

NUMBER = random.randint(1, 100)

def guess_the_number():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    while True:
        try:
            result = int(input("Guess the number: "))
        except ValueError:
            return print("It's not a number")
        if result > NUMBER:
            print("Too high.")
        elif result < NUMBER:
            print("Too low.")
        elif result == NUMBER:
            return print("You guessed right!")


if __name__ == '__main__':
    guess_the_number()

