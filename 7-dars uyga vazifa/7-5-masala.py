number = int(input("Raqamni kiriting: "))
summ = 1
for fac in range(1, number+1):
    summ *= fac
    
print(number, "soning faktoriali", summ, " ga teng.")