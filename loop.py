colours = ["Red", "Blue", "Green", "Pink", "Black"]

string = ""
for colour in colours:
    isFirst = colours[0] == colour
    isLast = colours[len(colours) -1] == colour

    if isFirst:
        string = f"My favourite colour is {colour}."
        continue

    if isLast:
        string = f"{string} Actually, no it's really {colour}. :)"
        continue

    string = f"{string} No, wait! It's actually {colour}."

print(string)