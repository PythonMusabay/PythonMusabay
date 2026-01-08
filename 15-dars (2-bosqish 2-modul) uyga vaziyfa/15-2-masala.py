number_list = ["Temur", "Muhtor", "Amir", "Siroj", "Aziz",
                "Farruh", "Kamola", "Sitora"]
new_list = []
for i in range(len(number_list)):
    if i % 2 == 0:
        new_list.append(number_list[i])

print(new_list)