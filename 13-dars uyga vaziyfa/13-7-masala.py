d_from = 0
d_to = 4
max_danger = float(input("Yo'l qo'yilishi mumkin bo'lgan eng yuqori havf darajasini kirirting: "))
depth = d_from + (d_to - d_from) / 2
danger = depth ** 3 - 3 * depth ** 2 - 12 * depth + 10

if max_danger < 0:
    print("Xato: Yo'l qo'yilishi mumkin bo'lgan eng yuqori havf darajasi "
    "   - mutloq kattalik va noldan kattaroq bo'lishi kerak.")
else:
    #print("Depth", depth, "Danger", danger)

    while abs(danger) > max_danger:
        if  danger > 0:
            d_from = depth
        else:
            d_to =depth

        depth = d_from + (d_to - d_from) / 2
        danger = depth ** 3 - 3 * depth ** 2 - 12 * depth + 10
        #print("Depth", depth, "Danger", danger)

print("Havfsiz tuqum qo'yishning taxminiy chuqurligi:", depth, "metr")