
first_number = float(input("Birinchi sonni kirirting: "))
second_number = float(input("Ikkinchi sonni kiriting: "))

first_num = int(first_number)       # berilgan 1-sonning butun qismi
second_num = int(second_number)     # berilgan 2-sonning butun qismi

first_fraction_part = round(first_number % 1, 2)      # berilgan 1-sonning qoldiq qismi
second_fraction_par = round(second_number % 1, 2)     # berilgan 2-sonning qoldiq qismi

first_reverse_number = ((first_num % 10) * 100 + ((first_num % 100) // 10) * 10 
                            +(first_num // 100)) + (((first_fraction_part * 100) % 10) * 10 +((first_fraction_part * 100) // 10)) / 100
second_reverse_number = ((second_num % 10) * 100 + ((second_num % 100) // 10) * 10 
                            +(second_num // 100)) + (((second_fraction_par * 100) % 10) * 10 +((second_fraction_par * 100) // 10)) / 100

print("Birinchi son teskari:", first_reverse_number)
print("Ikkinchi son teskari:", second_reverse_number)
print("Yig'indi: ", first_reverse_number + second_reverse_number)