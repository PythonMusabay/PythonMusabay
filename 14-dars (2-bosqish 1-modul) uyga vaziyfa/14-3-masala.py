number = int(input("Sonni kiriting: "))

def add(number):
    first_summ = 0
    while number > 0:
        first_summ += number % 10
        number //= 10

    print("Sonlar yig'indisi: ", first_summ)
add(number)


def number_of_digits(number):
    first_summ = 0
    second_summ = 0
    while number > 0:
        second_summ += 1
        first_summ += number % 10
        number //= 10

    print("Sondagi raqamlar miqdori: ", second_summ)
    print("Sonlar yig'indisi va raqamlar miqdorining ayirmasi: ", first_summ - second_summ)
number_of_digits(number)


