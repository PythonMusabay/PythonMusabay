number_films = int(input("Nechta fimlarni qo'shishni xoxlaysiz?  "))
films = ["Qattiq yong'oq", "O'tmishga qaytish", "Taksichi", "Leon", "Bogema rapsodiyasi", 
         "Gunohlar shahri", "Memento", "Otstupnuki", "Qishloq"]
new_list = []

for i in range(number_films):
    new_films = input("Film nomini kiriting: ")
    if new_films in films:
        new_list.append(new_films)
    else:
        print("Xato: ", new_films, "filmi yo'q" )
    
print("Sizning sevimli filmlaringiz ro'yxati", new_list)
