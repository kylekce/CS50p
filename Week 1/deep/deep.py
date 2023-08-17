prompt = input("What is the answer to the Great Question of Life, the Universe and Everything? ").strip()

if prompt.isnumeric() and int(prompt) == 42:
    print("Yes")
elif prompt.lower() == "forty-two" or prompt.lower() == "forty two":
    print("Yes")
else:
    print("No")