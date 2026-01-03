first_number = float(input("Birirnchi sonni kirirting: "))
second_number = float(input("Ikkinchi sonni kiriting: "))
def minimum(first_number, second_number):
    num = ((first_number + second_number) - abs(first_number-second_number)) / 2
    print("Eng kichik son: ", num)
minimum(first_number, second_number)
