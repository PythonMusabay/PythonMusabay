time = int(input("Bomba portlashigacha bo'lgan vaqtni kiriting: "))
summ = 0
summ_1 = 0
for i in range(time, 0, -1):
    summ += 1
    if time - summ != 0:
        bom = int(input("Zararsizlantirishni xohlaysizmi yoki o'yin atmosferasini kuchaytirishda davom etasizmi? "))
        if bom != 0:
            summ_1 += bom
            print(time - (time - i), "soniya oldin zararsizlantirildi")
            break
    else:
        print("Bopba portladi")
