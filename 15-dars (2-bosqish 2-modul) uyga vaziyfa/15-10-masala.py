number = int(input("Neshta elementdan iborat bo'lsin: "))
number_list = []


for i in range(number):
    print("Ro'yqatning", i+1, "elementin kirirting: ", end="")
    num = int(input())
    number_list.append(num)

print("Boshlang'ich ro'yxat: ", number_list)
number_list.sort()    # bu erda sort() metodi ro'yqatni o'sish tartibida joylashtiradi
print("Saralangan ro'yxat: ", number_list)

