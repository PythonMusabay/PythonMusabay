number = int(input("Hujayralar soni: "))
new_list = []
summ = 0
for i in range(number):
    print(i+1, "hujayra mahsuldorligi: ", end="")
    num = int(input())
    if i >= num:
        new_list.append(num)
print("To'g'ri kelmaydigan qiymatlar: ", new_list)

