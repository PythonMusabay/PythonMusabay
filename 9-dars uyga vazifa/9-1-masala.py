text = input("Hafta kunlarin kiriting: ")
summ = 1
days = ["dushanba", "seshanba", "chorshanba", "payshanba", "juma", "shanba", "yakshanba"]
for symbol in days:
  if symbol == text:
    print("Hafta kuninig raqami:", summ)
  else:
    summ += 1