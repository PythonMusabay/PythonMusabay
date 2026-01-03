first_number = float(input("X ni kiriting: "))
second_number = float(input("Y ni kiriting: "))

def coordinat(first_number, second_number):
    if abs(first_number) <= 1 and abs(second_number) <= 1:
        print("Tangacha shu yaqinda")
    else:
        print("Ushbu joyda tangacha yo'q")
        

coordinat(first_number, second_number)