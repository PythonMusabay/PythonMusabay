conteyner = int(input("Konteynerlar soni: "))
new_list = []
for _ in range(conteyner):
    new_number = int(input("Konteyner vaznini kiritish: "))
    if new_number < 200:
        new_list.append(new_number)
    else:
        print("massa 200 dan oshmasligi kerak !")
        new_number = int(input("qaytadan kiriting: "))
        conteyner += 1
num_number = int(input("Yangi konteynerning vaznini kiritish: "))
summ_first = 1
summ_second = 0
for i in new_list:
    summ_first += 1
    if num_number < i:
       summ_second = summ_first
print("Yangi konteyner raqami ", summ_second)