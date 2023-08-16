def main():
    input_text = input()
    convert(input_text)

def convert(text):
    modified_text = text.replace(":)", "🙂").replace(":(", "🙁")
    print(modified_text)

main()