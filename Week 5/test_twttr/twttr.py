def main():
    prompt = input("Input: ")
    print("Output:", shorten(prompt))


def shorten(word):
    output = []
    for n in word:
        if n.lower() not in ["a", "e", "i", "o", "u"]:
            output.append(n)
    return "".join(output)


if __name__ == "__main__":
    main()
