def repeater(word):
    garage_0 = []

    for char in word:
        garage_0.append(char)

    garage_1 = set()
    unix = []

    for z in garage_0:
        if z not in unix:
            unix.append(z)
            garage_1.add(z)

    print("I am first repeater in my family ", unix[0])
    return unix[0]