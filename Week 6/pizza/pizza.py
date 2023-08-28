import sys
import csv
from tabulate import tabulate

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")

try:
    with open(sys.argv[1], "r") as file:
        reader = csv.DictReader(file)

        table = []

        for row in reader:
            table.append([row[reader.fieldnames[0]], row[reader.fieldnames[1]], row[reader.fieldnames[2]]])
        
        print(tabulate(table, headers=[reader.fieldnames[0], reader.fieldnames[1], reader.fieldnames[2]], tablefmt="grid"))

except FileNotFoundError:
    sys.exit("File does not exist")
