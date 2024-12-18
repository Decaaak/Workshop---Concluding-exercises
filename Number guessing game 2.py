def user():
    poss_input = ["too small","too big","you win"]
    while True:
        user_answer = input().lower()
        if user_answer in poss_input:
            break
        print("input is invalid")
    return user_answer





def guess_the_number():
    print("Think about a number between 0 and 1000,and let me guess it :)")
    print()
    min_number = 0
    max_number = 1000
    user_answer = ""
    while user_answer != "you win":
        guess = (max_number - min_number) // 2 + min_number
        print(f"Your number is: {guess}")
        user_answer = user()
        if user_answer == "too big":
            max_number = guess
        elif user_answer == "too small":
            min_number = guess
    print("I quessed")





















if __name__ == '__main__':
    guess_the_number()