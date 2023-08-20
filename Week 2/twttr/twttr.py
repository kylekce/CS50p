prompt = input("Input: ")

output = []
for n in prompt:
    if n.lower() not in ["a", "e", "i", "o", "u"]:
        output.append(n)

print("Output:","".join(output))