text = input("Qatorlarni kiriting: ")
first_summ = 0
second_summ = 1
for symbol in text:
    if symbol == "b":
        first_summ += 2 * second_summ
    second_summ += 1

print("Bir kunda", first_summ, " litr sut ishlab chiqarilgan")

       


        
        
            