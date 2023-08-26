def main():
    while True:
        try:
            prompt = input("Fraction: ")

            x, y = prompt.split("/")
            if int(x) > int(y):
                continue

            percentage = convert(prompt)
            print(gauge(percentage)) 
        except (ValueError, ZeroDivisionError):
            pass
        else:
            break


def convert(fraction):
    x, y = fraction.split("/")
    return round((int(x) / int(y)) * 100)


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return str(percentage) + "%"


if __name__ == "__main__":
    main()
