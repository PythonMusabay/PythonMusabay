text = input("Matnni kiriting: ")
first_summ = 0
second_summ = 0
print("\n", end = "")
for symbol in text:
  if symbol != " ":
    first_summ += 1
  else:
    if first_summ > second_summ:
      second_summ = first_summ
    first_summ = 0

if second_summ > first_summ:
  print("Eng uzun so`zning uzunligi: ", second_summ)
else:
  print("Eng uzun so`zning uzunligi: ", first_summ)
