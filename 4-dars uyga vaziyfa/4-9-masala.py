first_number = int(input("Bosib o'tilgan: "))   # bu erda son uch xonali bo'lishi kerak
second_number = int(input("Kun raqami: "))
summ_1 = first_number // 100 + (first_number // 10) % 10 + first_number % 10
#print(summ_1)
if summ_1 > second_number:
    print("Sonlarni tashlab yuborish")
    print("Bosib o'tilgan yo'l", 0, "ga teng")
else:
    print("Bugun buzilmadi")
