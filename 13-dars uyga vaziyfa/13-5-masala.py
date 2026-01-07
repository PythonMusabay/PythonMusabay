first_number = int(input("Birinchi sonni kiriting: "))
summ = 0
temp = first_number
def new_number(number):
  last_digit = number % 10
  first_digit = number // 10 ** (summ - 1)
  between_digits = number % 10 ** (summ - 1) // 10
  number = last_digit * 10 ** (summ - 1) + between_digits * 10 + first_digit
  return number
while temp > 0:
    summ += 1
    temp = temp // 10

if summ < 3:
    print("Birinchi sondagi raqamlar soni uchtadan kam.")
else:
    first_number = new_number(first_number)
    print("O'zgartirilgan birinchi son:", first_number)
    second_number = int(input("\nIkkinchi sonni kiriting: "))
    summ = 0
    temp = second_number
    
    while temp > 0:
        summ += 1
        temp = temp // 10
    if summ < 4:
        print("Ikkinchi sondagi raqamlar soni to‘rttadan kam.")
    else:
        second_number = new_number(second_number)
        print("O'zgartirilgan ikkinchi son:", second_number)
        print("\nSonlar yig'indisi:", first_number + second_number)