number = int(input("Raqamni kiriting: "))
summ = 1

while  number != 7:
    summ += 1
    
    if number > 7:
        print("Raqam kerak bo'lganidan ko'proq. Yana bir bor urinib ko`ring!")
        number = int(input("Raqamni kiriting: "))

    else:
        print("Raqam kerak bo'lganidan kamroq. Yana bir bor urinib ko`ring!")
        number = int(input("Raqamni kiriting: "))
   

print("Siz topdingiz! Urinishlar soni: ", summ)