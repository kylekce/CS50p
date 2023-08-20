def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.
    if not(2 <= len(s) <= 6):
        return False
    
    # All vanity plates must start with at least two letters
    if not (s[0].isalpha() and s[1].isalpha()):
        return False
    
    # Numbers cannot be used in the middle of a plate; they must come at the end
    digit_flag = False
    digits = []
    for i in range(len(s) - 1):
        if s[i].isdigit():
            digit_flag = True
            digits.append(s[i])
        if digit_flag and s[i].isalpha():
            return False
        
    # The first number used cannot be a ‘0’.
    if len(digits) > 0:
        if digits[0] == '0':
            return False

    # No periods, spaces, or punctuation marks are allowed.
    if s.find('.') != -1 or s.find(' ') != -1 or s.find(',') != -1:
        return False

    # If the plate is valid, return True
    return True

main()