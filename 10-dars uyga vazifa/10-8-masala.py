number = int(input("Raqamni kiriting: "))
for row in range(1, number+1, 2):
    for col in range(number+1, 0, -1):
        if row >= col:
           print("#", end="")
           print(" ", end="")
          
           
        else:
            print(" ", end="")
      
    print()
  
        