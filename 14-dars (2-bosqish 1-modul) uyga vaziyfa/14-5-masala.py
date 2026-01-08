def smallest_divisor(number):
    for i in range(2, number + 1):
        if number % i == 0:
            return i

number = int(input("Sonni kiriting: "))
num = smallest_divisor(number)
print("Birdan farq qiluvchi eng kichik bo'luvchi:", num)