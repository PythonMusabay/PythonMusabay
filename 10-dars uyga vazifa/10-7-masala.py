number = int(input("Nechta son kiritasiz? "))
summ = 0
max_summ = 0
max_number = 0
for counter in range(number):
  new_number = int(input("Soni kiriting : "))
  s = new_number
  while s > 0:
    summ += s % 10
    s //= 10
  if summ > max_summ:
    max_summ = summ
    summ = 0
    max_number = new_number
  else:
    summ = 0
print("Eng katta son: ", max_number, "raqamlar yig`indisi: ", max_summ)