expon = input("Sonni kiriting: ")
mantis = " "
exp = " "
summ = 0
for i in expon:
  if summ == 0 and i != "e":
    mantis += i
  elif summ == 1:
    exp += i
  else:
    summ += 1
print("Sonning mantissasi: ", mantis)
print("Sonning exponenti: ", exp)
