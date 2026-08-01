for i in range(5):

    # H
    for j in range(5):
        if j == 0 or j == 4 or i == 2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print("  ", end="")

    # A
    for j in range(5):
        if (i == 0 and j == 2) or \
           (j == 0 and i != 0) or \
           (j == 4 and i != 0) or \
           (i == 2):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print("  ", end="")

    # S
    for j in range(5):
        if i == 0 or i == 2 or i == 4 or \
           (j == 0 and i < 2) or \
           (j == 4 and i > 2):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print("  ", end="")

    # I
    for j in range(5):
        if i == 0 or i == 4 or j == 2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print("  ", end="")

    # B
    for j in range(5):
        if j == 0 or \
           (i == 0 and j < 4) or \
           (i == 2 and j < 4) or \
           (i == 4 and j < 4) or \
           (j == 4 and i != 0 and i != 2 and i != 4):
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()