max_x = 15
max_y = 20
min_x = 1
min_y = 1

# Boshlang'ich pozitsiya
x = 8
y = 10

while True:
    print(f"Marsoxod {x}, {y} pozitsiyasida joylashgan, buyruqni kiriting:")
    command = input()#.upper()  

    if (command == "W") or (command == "w"):      # Shimol
        if y < max_y:
            y += 1

    elif (command == "S") or (command == "s"):     # Janub
        if y > min_y:
            y -= 1

    elif (command == "A") or (command == "a"):     # G'arb
        if x > min_x:
            x -= 1

    elif (command == "D") or (command == "d"):      # Sharq
        if x < max_x:
            x += 1

    else:
        print("Noto'g'ri buyruq!")