import sys
import csv

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

try:
    with open(sys.argv[1], "r") as before:
        with open(sys.argv[2], "w") as after:
            reader = csv.DictReader(before)
            writer = csv.DictWriter(after, fieldnames=["first", "last", "house"])

            writer.writeheader()
            for row in reader:
                last, first = row["name"].split(sep=",")
                first = first.strip()
                house = row["house"]

                writer.writerow({"first": first, "last": last, "house": house})
except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")
