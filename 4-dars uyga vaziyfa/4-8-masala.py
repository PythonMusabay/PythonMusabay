hours = int(input("Ishlagan soatlarni kiriting: "))
credit = int(input("Kredit bo‘yicha qoldiqni kiriting: "))
food = int(input("Ovqatlanish xarajatlari: "))
summ = (200 * hours)/(2**3) +hours
if summ <= food:
    print("Soatlar yetarli emas. Ishlash kerak!")
else:
    print("Soatlar yetarli, dam olish mumkin")