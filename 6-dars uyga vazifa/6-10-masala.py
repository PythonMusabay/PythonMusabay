low = 1
high = 100
n = (low + high) // 2

while True:
  print("Sizning raqamingiz tengmi, kichikmi, kattami?", n)
  answer = int(input("1-teng, 2-katta, 3-kichik: "))
  if answer == 1:
    print("Men topdim!")
    break
  elif answer == 2:
    low = n + 1
    n = (low + high) // 2
  else:
    high = n - 1
    n = (low + high) // 2
