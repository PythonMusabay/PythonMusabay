number = int(input("Qarzdorlar sonini kiriting: "))
summ = 0
for num in range(0, number+1, 5):
    print(num, "-raqamli qarzdor")
    debtor = int(input("Qancha qarz? "))
    summ += debtor
print("Qarzning umumiy miqdori: ", summ)


