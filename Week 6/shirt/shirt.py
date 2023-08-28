import sys
from PIL import Image, ImageOps

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif not sys.argv[1].lower().endswith(".jpg") or sys.argv[2].lower().endswith(".jpeg") or sys.argv[1].lower().endswith(".png"):
    sys.exit("Invalid input")

input_name, input_type = sys.argv[1].split(sep=".")
output_name, output_type = sys.argv[2].split(sep=".")
if input_type != output_type:
    sys.exit("Input and output have different extensions")

try:
    # Open the images
    before = Image.open(sys.argv[1])
    shirt = Image.open("shirt.png")

    # Resize the image
    before = ImageOps.fit(before, shirt.size)

    # Paste the shirt on the before image
    before.paste(shirt, mask=shirt)

    # Save the image
    before.save(sys.argv[2])

except FileNotFoundError:
    sys.exit("Input does not exist")
