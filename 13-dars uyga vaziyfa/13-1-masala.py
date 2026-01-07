number = float(input("Sonni kiriting: "))
summ = 0
if number >= 10:
  while number >= 10:
    summ += 1
    number /= 10
elif number < 1:
  while number < 1:
    summ -= 1
    number = number * 10
    
print("Suzuvchi nuqta format : x = ", number, "* 10 ** ", summ)
