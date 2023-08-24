names = []

while True:
    try:
        name = input("Name: ")
        names.append(name)

    except EOFError:
        output = "Adieu, adieu, to " + names[0]
        print(f"\n{output}")

        for i in range(1, len(names)):
            if len(names) == 2:
                output += " and " + names[i]
                print(output)
                break
            elif i == len(names) - 1:
                output += ", and " + names[i]
                print(output)
                break
            else:
                output += ", " + names[i]
                print(output)
        break
