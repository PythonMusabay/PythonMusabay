new_number = int(input("Surish: "))
first_list = []
second_list = []

for i in range(5):
    print("Ro'yqatning", i+1, "elementin kirirting: ", end="")
    number = int(input())
    first_list.append(number)

for num in range(len(first_list)):
    second_list.append(first_list[num - new_number])

print("Boshlang'ich ro'yxat: ", first_list)
print("Surilgan ro'yxat:", second_list)

