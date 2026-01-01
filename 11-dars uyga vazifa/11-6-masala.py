print("Kiritish:")
lower_limit = int(input("Quyi chegarani kiriting: "))
upper_limit = int(input("Yuqori chegarani kiriting: "))
step = int(input("Qadamni kiriting: "))

print("Chiqarish:") 
for i in range(lower_limit, upper_limit, step):
    print(i,"C", i * 1.8 + 32, 'F') 
print(upper_limit, 'C', upper_limit * 1.8 + 32, 'F')

    