number = int(input("Sonni kiriting: "))
a = number // 1000
b = (number % 1000) // 100
c = (number % 100) //10
d = number % 10 
print(d * 1000 + c * 100 + b * 10 + a)