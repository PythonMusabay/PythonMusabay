first_number = int(input("Birinchi sonni kiriting: "))
second_number = int(input("Ikkinchi sonni kiriting: "))
summ_1 = 0
summ_2 = 0
for number in range(first_number, second_number+1):
    
    if number % 3 == 0:
        summ_2 += number
        summ_1 += 1
print(summ_2 / summ_1)

