print("Otning turgan joyini kiriting:")
x_1 = float(input())
y_1 = float(input())

print("Doskadagi nuqtaning turgan joyini kiriting:")
x_2 = float(input())
y_2 = float(input())

x_1 = int(x_1 * 10) 
y_1 = int(y_1 * 10)
x_2 = int(x_2 * 10)
y_2 = int(y_2 * 10) 

print("Qafasdagi ot (", x_1, ",", y_1, "). Qafasdagi nuqta (", x_2, ',', y_2,').')
if (abs(x_2 - x_1) == 1 and abs(y_2 - y_1) == 2) or (abs(x_2 - x_1) == 2 and abs(y_2 - y_1) == 1):
  print("Ha, ot bu nuqtaga yura oladi")
else:
  print("Yo`q bu nuqtaga yura olmaydi")