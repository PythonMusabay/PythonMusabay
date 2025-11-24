text_number = int(input("Tajriybalar sonin kiriting: "))
if text_number < 1000:
    print("Sizning bosqichingiz: ", 1)
elif text_number >= 1000 and text_number < 2500:
    print("Sizning bosqichingiz: ", 2)
elif text_number >= 2500 and text_number <= 5000:
    print("Sizning bosqichingiz: ", 3)
else:
    print("Sizning bosqichingiz: ", 4)  
