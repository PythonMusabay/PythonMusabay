file_size = int(input("Yuklab olish uchun fayl hajmini ko'rsating: "))
speed = int(input("Ulanish tezligingiz qanday? "))
summ = 0

for num in range(1, file_size+1):
    summ += speed

    if num * speed < file_size:
        print(num,"sekund o'tdi. 123 MBdan", summ, "MB yuklab olindi", "(", round(num * speed * 100 / file_size), "%)")
             
    else:
         print(num,"sekund o'tdi. 123 MBdan", file_size, "MB yuklab olindi", "(100%)")
         break
    #print()
                
    
    