for row in range(11):
    for col in range(30):
        if col == 0 or col == 29:
            print("|", end="")
        elif row == 0 or row == 10:
            print("-", end="")
        else:
            print(" ", end="")
    print()

       


