import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    try:
        src = re.search(r'src="(.+?")', s).group(1)
        id = re.search(r'embed/(.+?)"', src).group(1)
    except AttributeError:
        return None
    else:
        return f"https://youtu.be/{id}"


if __name__ == "__main__":
    main()
