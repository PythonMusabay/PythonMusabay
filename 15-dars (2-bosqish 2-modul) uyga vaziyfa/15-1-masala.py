number = int(input("Sonni kiriritng: "))
new_list = []

for i in range(1, number+1):
    if i % 2 != 0:
        new_list.append(i)
print(new_list)