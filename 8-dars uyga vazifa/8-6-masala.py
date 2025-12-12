letter = int (input ("Xatning kvadrat o'lchami: "))
summ = 0  
s = letter // 2
for number in range(letter, 12, -s): 
  summ += 2 
  
print("Xat", summ , "marta buklandi")