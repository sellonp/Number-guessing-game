import random
def number_guessing():
    while True:
        print("select the difficulty level")
        print("1.Easy, unlimited attempts")
        print("2.Medium, 10 attempts")
        print("3.Hard, 5 attempts")

        Level = int(input("Enter a difficulty level(1-3): "))

        if Level == 1:
            secret_number = random.randint(1, 100)
            attempts = 0
            while True:
                try:
                    user_guess = int(input("Enter a number:"))
                    attempts += 1
                    if user_guess < secret_number:
                        print("number too low")
                    elif user_guess > secret_number:
                        print("Number too high")
                    else:
                        print(f"You guessed it correctly in {attempts} attempts")
                        break
                except ValueError:
                    print("Enter a valid number")
        elif Level == 2:
            secret_number = random.randint(1, 100)
            attempts = 0
            while attempts < 10:
                try:
                    user_guess = int(input("Enter a number:"))
                    attempts += 1
                    if user_guess < secret_number:
                        print("number too low")
                    elif user_guess > secret_number:
                        print("Number too high")
                    else:
                        print(f"You guessed it correctly in {attempts} attempts")
                        break
                    if attempts == 10:
                        print("You didn't guess anymore")
                except ValueError:
                    print("Enter a valid number")
        elif Level == 3:
            secret_number = random.randint(1, 100)
            attempts = 0
            while attempts < 5:
                try:
                    user_guess = int(input("Enter a number:"))
                    attempts += 1
                    if user_guess < secret_number:
                        print("number too low")
                    elif user_guess > secret_number:
                        print("Number too high")
                    else:
                        print(f"You guessed it correctly in {attempts} attempts")
                        break
                    if attempts == 5:
                        print("You didn't guess anymore")

                except ValueError:
                    print("Enter a valid number")
        else:
            print("Enter a valid number")
            continue

        play_again = input("Do you want to play again? (y/n):").lower()
        if not play_again.startswith("y"):
            print("Thank for playing")
            break

if __name__ == '__main__':
    number_guessing()