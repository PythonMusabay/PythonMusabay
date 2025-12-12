begin_number = int(input("a sonin kiriting: "))
end_number = int(input("b sonin kiriting: "))
multiple_number = int(input("Qaysi songa karrali bo'lsin? "))
summ = 0
number_of_cycles = 0

for number in range(begin_number, end_number+1):
    if number % multiple_number == 0:
        number_of_cycles += 1
        summ += number
 
print("O'rtacha arifmetik qiymati", summ / number_of_cycles)