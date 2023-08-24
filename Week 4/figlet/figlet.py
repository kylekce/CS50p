import sys
import random
from pyfiglet import Figlet

if len(sys.argv) == 1:
    prompt = input("Input: ")

    f = Figlet(font=random.choice(Figlet().getFonts()))
    print("Output:", f.renderText(prompt))
elif len(sys.argv) == 3:
    if sys.argv[1] not in ["-f", "--font"]:
        sys.exit("Invalid usage")
    elif sys.argv[2] not in Figlet().getFonts():
        sys.exit("Invalid usage")
    else:
        prompt = input("Input: ")

        f = Figlet(font=sys.argv[2])
        print("Output:", f.renderText(prompt))
else:
    sys.exit("Invalid usage")
