def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # TODO
    result = d.replace("$", "")
    return float(result)


def percent_to_float(p):
    # TODO
    result = p.replace("%", "")
    return float(result) / 100


main()