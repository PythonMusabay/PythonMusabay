number = int(input("Nechta sonni kiritasiz? "))
summ = 0
for i in range(number):
  new_number = int(input("Soni kiriting: "))
  div = new_number // 2
  while div > 1:
    if new_number % div == 0:
      summ += 1
      break
    else:
      div -= 1
print("Ketma - ketlikdagi oddiy raqamlar soni -", number - summ)
