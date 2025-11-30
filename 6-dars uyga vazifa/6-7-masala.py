print("8-soatlik ish kuni boshlandi")

hour = 0
summ = 0

while hour != 8:
    hour += 1
    print(hour, "-soat")
    num = int(input("Bobur nechta vazifani bajardi? "))
    summ += num
    text = int(input("Xotini qo'ng'iroq qilmoqda. Javob berish kerakmi? (1 -ha, 0 -yo'q): "))

if text != 0:
    print("Ish vaqti tugadi. Jami bajarilgan vazifalar soni: ", summ)
    print("Do'konga kirish kerak")

else:
    print("Ish vaqti tugadi. Jami bajarilgan vazifalar soni: ", summ)
    #print("Do'konga kirish kerak")
   
  