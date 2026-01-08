import math
print("Tangachaning koordinatalarini kiriting: ")

coor_number_x = float(input("X: "))
coor_number_y = float(input("Y: "))
radius = float(input("Radiusni kiriting: "))

if radius >= math.sqrt(coor_number_x ** 2 + coor_number_y ** 2):
    print("Tangacha qaerdadir shu atrofda")
else:
    print("Tangacha bu atrofda yo'q")