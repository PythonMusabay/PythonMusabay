number = float(input("Musbat sonni kirirting: "))
num = round(number, 1)
#print(round(number, 1))

print("Berilgan sonning o'nlik nuqtadan keyin uning birinchi raqami: ", int((num * 10) % 10))