home_metrs= int(input("Xonaning metr kvadarati: "))
home_summ = int(input("Uyning narxi: "))
if (home_metrs >= 80  or home_metrs < 100) and home_summ < 10000000:
    print("To'g'ri keladi") 
elif home_metrs < 80 and home_summ < 7000000:
    print("To'g'ri keladi")
else:
    print("To'g'ri kelmaydi")