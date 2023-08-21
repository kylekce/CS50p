months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        prompt = input("Date: ")

        if prompt.find("/") >= 0:
            m, d, y = prompt.strip().split("/")

            if int(m) > 12 or int(d) > 31:
                continue

            m = "0" + m if len(m) == 1 else m
            d = "0" + d if len(d) == 1 else d

            print(f"{y}-{m}-{d}")
            break

        elif prompt.find(" ") >= 0:
            m, d, y = prompt.split(" ")
            m = months.index(m) + 1

            if d.find(",") < 0:
                continue
            else:
                d = d.replace(",", "")

            if int(m) > 12 or int(d) > 31:
                continue

            m = "0" + str(m) if len(str(m)) == 1 else m
            d = "0" + d if len(d) == 1 else d

            print(f"{y}-{m}-{d}")
            break
    except (ValueError):
        continue
    except EOFError:
        break
