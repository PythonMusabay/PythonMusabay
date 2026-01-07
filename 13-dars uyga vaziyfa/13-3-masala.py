first_number = int(input("Birirnchi sonni kirirting: "))
second_number = int(input("Ikkinchi sonni kirirting: "))
first_reverse_number = (first_number % 10) * 100 + ((first_number // 10) % 10) * 10 + first_number // 100
second_reverse_number = (second_number % 10) * 100 +((second_number // 10) % 10) * 10 + second_number // 100
print("Birinchi songa teskari son:", first_reverse_number)
print("Ikkinchi songa teskari son:", second_reverse_number)
print("Yig'indi:",first_reverse_number + second_reverse_number)
print("Yig'indiga teskari son:", first_number + second_number)
