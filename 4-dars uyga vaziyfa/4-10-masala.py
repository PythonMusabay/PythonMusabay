first_number = int(input("Birinchi sonni kiriting: "))
second_number = int(input("Ikkinchi sonni kiriting: "))
third_number = int(input("Uchunchi sonni kiriting: "))
if first_number > second_number:
    maximum = first_number
else:
    maximum = second_number
if third_number > maximum:
      maximum = third_number
print("Maksimal son", maximum)

