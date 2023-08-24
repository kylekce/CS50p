from random import randint

def game(n):
    while True:
        try:
            guess = input("Guess: ")

            if not guess.isdigit():
                continue
            elif int(guess) < 1:
                continue
            else:
                guess = int(guess)

            if guess == randint(1, int(n)):
                print("Just right!")
                break
            elif guess > randint(1, int(n)):
                print("Too large!")
            elif guess < randint(1, int(n)):
                print("Too small!")
        except ValueError:
            continue

while True:
    level = input("Level: ")

    if level.isnumeric():
        game(int(level))
        break
    else:
        continue
