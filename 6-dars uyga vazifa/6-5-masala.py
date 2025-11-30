number = int(input("Chipta raqamni kiriting: "))  # bu erda 6 xonali son bo'lishi kerak
summ_1 = 0
summ_2 = 0
#print(((number // 1000) // 100))
#print(((number // 1000) // 10))
#print(((number // 1000) % 10))

#print(((number % 1000) // 100))
#print(((number % 1000) // 10) % 10)
#print(((number % 1000) % 10))

while number !=0:
    summ_1 = ((number // 1000) // 100) + ((number // 1000) // 10) % 10 + ((number // 1000) % 10)
    summ_2 = ((number % 1000) // 100) + ((number % 1000) // 10) % 10 + ((number % 1000) % 10)
    if summ_1 == summ_2:
        print("Omadli chipta")
    else:
        print("Omadli chipta emas")
    #print(summ_1)
    #print(summ_2)
    break

