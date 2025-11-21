first_product = int(input("Birinchi mahsulot narxi: "))
second_product = int(input("Ikkinchi mahsulot narxi: "))
third_product = int(input("Uchunchi mahsulot narxi: "))
summ = first_product + second_product + third_product
if summ >= 10000:
    print("Chegirma narxi:", summ - summ/100*10)
else:
    print("Umumiy narxi:", summ)
