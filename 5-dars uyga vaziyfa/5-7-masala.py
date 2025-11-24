first_number = int(input("Birinchi butun sonni kiriting: "))
second_number = int(input("Ikkinchi butun sonni kiriting: "))
third_number = int(input("Uchunchi butun sonni kiriting: "))
if first_number == second_number and first_number == third_number:
    print(3)
elif (first_number == second_number and second_number !=third_number) or (first_number == third_number and second_number != third_number) or (second_number == third_number and second_number != first_number):
    print(2)
else:
    print(0)