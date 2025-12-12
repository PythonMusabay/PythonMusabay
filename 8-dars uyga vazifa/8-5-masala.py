begin_number = int(input("Kesimning boshini kiriting: "))
end_number = int(input("Kesimtning oxirini kiriting: "))
step = int(input("Qadamni kiriting: "))

for number in range(end_number, begin_number-1, step):
    print(number, "-nuqtada funktsiya", number ** 3 + 2 * number ** 2 - 4 * number + 1, "ga teng")