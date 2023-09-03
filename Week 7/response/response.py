import validators

def main():
    validation((input("What's your email address? ")))


def validation(email):
    if validators.email(email):
        print("Valid")
    else:
        print("Invalid")


if __name__ == "__main__":
    main()
