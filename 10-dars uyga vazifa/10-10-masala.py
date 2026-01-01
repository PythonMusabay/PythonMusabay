number = int(input("Raqamni kiriting: "))
for row in range(number):
    for left_number in range(number, number-row-1, -1):
        print(left_number, end="")
    point_summ = 2 * (number - row -1)
    print("." * point_summ, end="")
    
    for right_number in range(number-row, number+1):
        print(right_number, end="")
    print()
