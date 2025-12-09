for number in range(10, 100):
    decimal = number // 10
    unity = number % 10
    if decimal * unity * 3 == number:
        print(number)
