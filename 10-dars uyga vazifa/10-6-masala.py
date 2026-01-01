number = int(input("Sonni kiriting: "))
first_summ = 1
second_summ = 0
for num in range(1, number+1):
    first_summ *= num
    second_summ += first_summ
    
print(second_summ)

