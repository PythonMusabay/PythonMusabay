text = input("So'zni kiriting: ")
text_list = []
summ = 0

for i in text:
    if text.count(i) == 1:
        summ += 1
        text_list.append(i)

print("Noyob harflar soni:", summ)
