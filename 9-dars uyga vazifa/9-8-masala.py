total_length = int(input("Kolontitulning umumiy uzunligini kiriting: "))  
number = int(input("Undov belgilari sonin kiriting: "))   

for i in range(total_length):  
    print(end="~")

for j in range(number):
    print(end="!")
      
for i in range(total_length):
    print(end="~")
