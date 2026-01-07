precision = float(input("Aniqlikni kiriting: "))
x = int(input("x ni kiriting : "))
first_summ = 1
second_summ= 2
while True:
  res = 1
  for i in range(1, second_summ + 1):
    res *= x / i
  if second_summ % 4 == 0:
    first_summ += res
  else:
    first_summ -= res
  second_summ += 2
  if abs(res) < precision:
    break
print("Qator yigindisi = ", first_summ)
