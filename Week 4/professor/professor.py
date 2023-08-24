import random


def main():
    level = get_level()
    correct_answers = 0
    tries = 0

    for i in range(10):
            x = generate_integer(level)
            y = generate_integer(level)
            z = x + y

            while True:
                try:
                    answer = int(input(f"{x} + {y} = "))

                    if answer == z:
                        correct_answers += 1
                        tries = 0
                        break
                    elif tries >= 2:
                        print(f"{x} + {y} = {z}")
                        tries = 0
                        break
                    else:
                        tries += 1
                        print("EEE")

                except ValueError:
                    tries += 1
                    print("EEE")

    print("Score:", correct_answers)

def get_level():
    while True:
        level = input("Level: ")

        if level in ["1", "2", "3"]:
            return int(level)

def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)

if __name__ == "__main__":
    main()
