number_of_rows = int(input("Qatorlar sonin kiriting: "))
number_of_seats_in_row = int(input("Qatordagi o'rindiqlar soni: "))   
number_of_spaces = int(input("Qatorlar orasidagi bo'sh metrlar masofasini kiriting: "))

print("Sahna")

for j in range(number_of_seats_in_row):
    print(end="\n")

    for i_1 in range(number_of_rows):
        print(end="=")
        
    for i_2 in range(number_of_spaces):
        print(end="*")
       
    for i_3 in range(number_of_rows):
        print(end="=")

                      