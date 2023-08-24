import requests
import sys

try:
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    else:
        try:
            n = float(sys.argv[1])
        except ValueError:
            sys.exit("Command-line argument is not a number")

        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        data = response.json()

        print(f"${n * data['bpi']['USD']['rate_float']:,.4f}")

except requests.RequestException:
    sys.exit("API request failed")
