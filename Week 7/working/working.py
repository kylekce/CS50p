import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    # Separate the start and end times
    hours = re.search(r"(.+) (AM|PM) to (.+) (AM|PM)", s)
    # If pattern did not match, raise ValueError
    if hours is None:
        raise ValueError("Invalid time format")
    else:
        starting_hour = hours.group(1)
        starting_meri = hours.group(2)
        ending_hour = hours.group(3)
        ending_meri = hours.group(4)

    # Separate the hours and minutes
    if re.search(r".+:.+", starting_hour):
        s1, s2 = starting_hour.split(":")
        e1, e2 = ending_hour.split(":")
    else:
        s1 = starting_hour
        s2 = "00"
        e1 = ending_hour
        e2 = "00"

    # Check for invalid times
    if int(s1) > 12 or int(e1) > 12 or int(s2) > 59 or int(e2) > 59:
        raise ValueError("Invalid time format")

    # Convert the start time
    if starting_meri == "PM":
        if s1 == "12":
            s1 = 12
        else:
            s1 = int(s1) + 12
    elif starting_meri == "AM" and s1 == "12":
        s1 = 00
    starting_hour = f"{int(s1):02}:{s2}"

    # Convert the end time
    if ending_meri == "PM":
        if e1 == "12":
            e1 = 12
        else:
            e1 = int(e1) + 12
    elif ending_meri == "AM" and e1 == "12":
        e1 = 00
    ending_hour = f"{int(e1):02}:{e2}"

    return f"{starting_hour} to {ending_hour}"


if __name__ == "__main__":
    main()
