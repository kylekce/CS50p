def main():
    time = input("What time is it? ")

    if 7.0 <= convert(time) <= 8.0:
        print("breakfast time")
    elif 12.0 <= convert(time) <= 13.0:
        print ("lunch time")
    elif 18.0 <= convert(time) <= 19.0:
        print("dinner time")

def convert(time):
    # If time is in 12 hour format
    if time.endswith("a.m.") or time.endswith("p.m."):
        x, y = time.split(" ")
        hour, minutes = x.split(":")
        # Convert hour to 24 hour format
        if y == "p.m.":
            hour = int(hour) + 12
    # If time is in 24 hour format
    else:
        hour, minutes = time.split(":")
    # Return time as a floating value
    return int(hour) + ((int(minutes) / 60))

if __name__ == "__main__":
    main()