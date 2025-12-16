text = input("Qatorni kiriting: ")
first_summ = 0
second_summ = 0

for symbol in text:
    if symbol == "s":
        first_summ += 1
        if first_summ > second_summ:
            second_summ = first_summ
    else:
        first_summ = 0

print("Eng uzun ketma-ketlik", second_summ)
