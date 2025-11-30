number = int(input("Raqamni kiriting: "))
number_exp = int(input("Sonning nechanchi darajasi: "))
num = 0
while num < number:
    num += 1
    summ = num ** number_exp
    print(num, "sonining", number_exp, "darajasi", summ)