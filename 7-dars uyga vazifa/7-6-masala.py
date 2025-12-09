number = int(input("O'quvchilar sonin kiriting: "))

first_summ = 0
second_summ = 0
third_summ = 0

for num in range(1, number+1):
    print(num, "- o'quvchi")
    text = int(input("Bahosin kiriting:"))
    if text > 4:
        first_summ += 1
    elif text == 4:
        second_summ += 1
    else:
        third_summ += 1

if first_summ >= second_summ:
    if second_summ >= third_summ:
        print("a'lo baho olgan o'quvchilar soni ko'p")
if first_summ <= second_summ:
    if second_summ >= third_summ:
        print("yaxshi baho olgan o'quvchilar soni ko'p")
if first_summ <= second_summ:
    if second_summ <= third_summ:
        print("uch baho olgan o'quvchilar soni ko'p")

#print("5 baho olgan o'quvchilar soni", first_summ)
#print("4 baho olgan o'quvchilar soni", second_summ)
#print("3 baho olgan o'quvchilar soni", third_summ)
