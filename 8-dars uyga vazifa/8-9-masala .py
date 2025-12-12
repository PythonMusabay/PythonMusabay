x = int(input("Sonni kiriting: "))
res = 1

for num in range(1, 7):
  res *= (x - (2 ** num - 1)) / (x - (2 ** num))
print(res)