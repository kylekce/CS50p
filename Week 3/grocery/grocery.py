groceries = []

while True:
    try:
        prompt = input().upper()
        groceries.append(prompt)

    except EOFError:
        groceries.sort()
        groceries_output = []

        for grocery in groceries:
            if grocery in groceries_output:
                continue
            else:
                groceries_output.append(grocery)
                print(groceries.count(grocery), grocery)
        break