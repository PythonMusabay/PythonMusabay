
number = int(input("Sonlar miqdorini kiriting: "))
import math
for i in range(number):
    num = float(input("Sonni kiriting: "))
   
    if num > 0:
        result_1 = math.ceil(num) 
        first_summ = math.log(result_1)
        print("x=", result_1, " log(x) =", first_summ)
       
      
    else:
        result_2 = math.floor(num) 
        second_summ = math.exp(result_2)
        print("x=", result_2, " exp(x) =", second_summ)


