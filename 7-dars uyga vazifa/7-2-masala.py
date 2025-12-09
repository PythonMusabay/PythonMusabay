summ = 0
for numbers in range(1, 11):
    number = int(input("Raqamni kiriting: "))
    if number % 2 == 0 and number > 0:
        print(numbers, "-raqam jup son")
        summ += 1
    else:
        print(numbers, "-raqam jup son emas")

print("Ularning", summ, "tasi juft")