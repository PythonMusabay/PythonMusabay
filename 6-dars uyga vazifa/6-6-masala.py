summ_1 = 0
summ_2 = 0
while True:
    number = int(input("Raqamni kiriting: "))
    if number == 0:
        break

    elif number > 0:
        summ_1 += 1
    else:
        summ_2 += 1
           
    
print("Musbat raqamlar soni: ", summ_1)
print("Manfiy raqamlar soni: ", summ_2)