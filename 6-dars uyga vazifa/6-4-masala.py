days = int(input("Kunni kiriting: "))
summ = 0
while days != 0:
  summ += days % 2 == 0
  days = int(input("Kunni kiriting: "))

print("Juft kunlarning umumiy soni", summ)
