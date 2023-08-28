import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif not sys.argv[1].endswith(".py"):
    sys.exit("Not a Python file")

try:
    with open(sys.argv[1], "r") as file:
        lines = file.readlines()

    count = 0

    for i in range(1, len(lines) + 1):
        # Comments
        if lines[-i].strip().startswith("#"):
            continue
        # Empty lines
        elif lines[-i].strip() == "":
            continue
        else:
            count += 1

    print(count)
except FileNotFoundError:
    sys.exit("File does not exist")
