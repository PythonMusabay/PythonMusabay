def count_letter(number,letter):
    number_summ = 0
    letter_summ = 0
    for i in text:
        if i == number:
            number_summ += 1
            #print(number, "raqami soni:", first_summ)
    for j in text:
        if j == letter:
            letter_summ += 1
            #print(letter, "harfi soni:", second_summ)
    
            
    print(number, "raqami soni:", number_summ) 
    print(letter, "harfi soni:", letter_summ) 

text = input("Matnni kiriting: ")
number = input("Qaysi sonni qidiryapmiz? ")
letter = input("Qaysi harfni qidiryapmiz? ")
count_letter(number,letter)





