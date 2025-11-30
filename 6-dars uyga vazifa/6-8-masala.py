deposit = int(input("Bankdagi omonat X dollarni kiriting: "))
percent = int(input("Yillik P foizni kiriting: "))
quantity = int(input("Y qiymatni kiriting: "))
summ = 0

while deposit < quantity:
    temp = deposit
    deposit = int(deposit + deposit * percent / 100)
    summ += 1
    

print("Necha yil kerak:", summ)