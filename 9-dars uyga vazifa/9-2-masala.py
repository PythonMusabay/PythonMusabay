summ = 0
for sym in range(11):
    text = input("Satrni kiriting: ")
    if (text == "karamba") or (text == "Karamba"):
        summ += 1
    else:
        continue

print("Karamba so'ziga mos keladigan ", summ, " ta so'z bor")