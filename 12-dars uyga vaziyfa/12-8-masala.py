first_number = int(input("Birinchi sonni kiriting: "))
second_number = int(input("Ikkinchi sonni kiriting: "))
def ekub(first_number, second_number):
    while first_number != 0 and second_number != 0:
        if first_number > second_number:
            first_number = first_number % second_number
        else:
            second_number = second_number % first_number
    print("Eng katta umumiy boluvchi: ", first_number + second_number)

ekub(first_number, second_number)