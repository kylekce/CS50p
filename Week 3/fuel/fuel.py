while True:
    try:
        prompt = input("Fraction: ")
        x, y = prompt.split("/")

        output = round((int(x) / int(y)) * 100)

        if int(x) > int(y):
            continue
        elif output <= 1:
            print("E")
        elif output >= 99:
            print("F")
        else:
            print(str(output) + "%")

    except (ValueError, ZeroDivisionError):
        pass
    else:
        break