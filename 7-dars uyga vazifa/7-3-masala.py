summ = 0
for mon in range(1, 13):
    print(mon, " - oy uchun qancha oylik Oldingiz? ")
    number = int(input())
    summ += number
print("Bir yil davomida o'rtacha oylik ish haqi", summ / 12)

