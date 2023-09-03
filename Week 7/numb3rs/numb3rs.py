import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    valid = re.search(r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(\.|$)){4}$", ip)
    if valid:
        return True
    else:
        return False


if __name__ == "__main__":
    main()
