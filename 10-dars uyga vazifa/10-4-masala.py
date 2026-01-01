for row in range(10):
    for col in range(10):
        if row == col:
            print("^", end = "")
        elif -col + 9 == row:
            print("^", end = "")
        else:
            print(" ", end = "")
    print()
               
           
   
        

       