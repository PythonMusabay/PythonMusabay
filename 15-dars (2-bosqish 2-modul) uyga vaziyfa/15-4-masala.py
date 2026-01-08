card_number = int(input("Videokartalar soni: "))
previous_list =[]
new_list =[]

for i in range(card_number):
    print(i+1, "-videokarta: ", end="")
    card = int(input())
    new_list.append(card)
    if new_list[i] == card:
        previous_list.append(card)
    
new_list = [i for i in previous_list if i != max(previous_list)]
print("Videokartalarning eski ro'yxati: ", previous_list)
print("Videokartalarning yangi ro'yxati: ", new_list)