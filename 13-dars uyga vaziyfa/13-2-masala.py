def max(a,b):
    max_number_1 = (a+b + abs(a-b))/2
    return max_number_1
  
first_number = int(input("Birirnchi sonni kirirting: "))
second_number = int(input("Ikkinchi sonni kiriting: "))
third_number = int(input("Uchunchi sonni kiriting: "))
max_number_1 = max(first_number,second_number)
max_number_2 = max(max_number_1, third_number)
print("Eng katta son: ", max_number_2)