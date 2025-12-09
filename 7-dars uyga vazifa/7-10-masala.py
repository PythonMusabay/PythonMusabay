
number = int(input("Kartalar sonin kiriting: "))
summ = number * (number + 1 ) // 2
remaining_summ = 0

for card in range(number-1):
    remaining_card = int(input("Qolgan kartani kiritish: "))
    remaining_summ += remaining_card
   
num = summ - remaining_summ
print("Yo'qolgan karta raqami: ", num)
