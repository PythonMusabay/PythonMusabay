number_sum= int(input("Ish haqini kiriting: "))
if number_sum <= 10000:
    print("Soliq stavkasi 13 % ni tashkil etadi:", number_sum * 13 / 100)
elif number_sum > 10000 and number_sum <= 50000:
    print("Soliq stavkasi 20 % ni tashkil etadi:", (number_sum - 10000) * 20 / 100 + 10000 * 13 / 100)
else:
    print("Soliq stavkasi 30 % ni tashkil etadi:", ((number_sum - 50000) * 30 / 100 )+ (((number_sum - 50000)-10000) * 20 / 100) + (10000 * 13 /100))


