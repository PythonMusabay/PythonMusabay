summ = 0
for sector in range(30, 36):
    print(sector, " - sektordagi odamlar soni:  ")
    number = int(input())
    if number <= 10:
        print("Hammasi joyida")
    else:
        print("Qoidabuzarlik! Sektordagi odamlar soni keragidan ko'p!")
        summ += 1
print("Qoidabuzarliklar soni: ", summ)

# "30-sektordagi odamlar soni: 7 ta."  shunaqa qilib bir qatorda chiqarsa bo'ladimi, menda keyingi qatorga tushib ketyapti