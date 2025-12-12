educational_grant = int(input("Stipendiyani kiriting: "))
expenses = int(input("Yashash xarajatlarini kiriting: "))
summ_1 = 0
summ_2 = 0
for number in range(1):
    summ_1 = expenses - educational_grant
    for num in range(1, 10):
        expenses *= 1.03
        summ_2 += expenses - educational_grant
print(summ_1 + summ_2)



