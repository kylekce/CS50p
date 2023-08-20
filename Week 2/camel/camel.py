prompt = input("camelCase: ")

result = []
for n in prompt:
    if n.isupper():
        result.append("_")
        result.append(n.lower())
    else:
        result.append(n)
print("snake_case:", "".join(result))
