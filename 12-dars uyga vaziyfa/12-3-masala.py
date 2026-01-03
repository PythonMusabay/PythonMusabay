number = int(input("Raqamni kiriting: "))
operate = input("Raqamlar yiginsisi uchun '+', maksimal raqam uchun 'max', minimal raqam uchun 'min': ")
def sum_number(number,summ):
  while number // 10 != 0:
    summ += number % 10
    number //= 10
  print("Raqamlar yig'indisi: ", summ + number)
def max_number(number):
  max = 0
  min = 0
  while number > 0:
    if max <= min:
      max = min
    min = number % 10
    number //= 10
  if max < min:
    max = min
  print("Eng katta raqam: ", max)
def min_number(number):
  min = 9
  while number > 0:
    max = number % 10
    if min >= max:
      min = max
    number //= 10
  print("Eng kichik raqam: ", min)
if operate == '+':
  summ = 0
  sum_number(number,summ)
elif operate == 'max':
  max_number(number)
elif operate == 'min':
  min_number(number)