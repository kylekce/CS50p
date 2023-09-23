from datetime import date
import sys
import inflect

p = inflect.engine()

def main():
    print_seasons(input("Date of birth: "))

    

def print_seasons(date_input):
    try:
        date_object = date.fromisoformat(date_input)
    except ValueError:
        sys.exit("Invalid date")

    date_difference = date.__sub__(date.today(), date_object)
    
    print(p.number_to_words(date_difference.days * 1440).capitalize().replace(" and", ""), "minutes")


if __name__ == "__main__":
    main()
