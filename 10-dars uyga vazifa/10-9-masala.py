number = int(input("Raqamni kiriting: "))
summ = -1
for row in range(1, number+1, 1):
    for col in range(number+1, 0, -1):
       
        if row >= col:
            summ += 2
            print(summ, end="   ")
            print("", end=" ")
                 
        else:
            print("", end="   ")
    print()
      
   