first_year = int(input("Birinchi yilni kiriting: "))
second_year = int(input("Ikkinchi yilni kiriting: "))
print("Uchta bir xil raqamlarga ega bo'lgan,", first_year, "-dan", second_year, "-gacha bo'lgan yillar:")

for i in range(first_year, second_year+1):
    a = i // 1000
    b = (i // 100) % 10
    c = (i % 100) // 10
    d = i % 10
    if a != b and b == c and c == d:
        print(a * 1000 + b * 100 + c * 10 + d)
    elif a == c and c == d and d != b:
        print(a * 1000 + b * 100 + c * 10 + d)
    elif a == b and b == c and c != d:
        print(a * 1000 + b * 100 + c * 10 + d)
    elif a == b and b == c and c == d:
        print(a * 1000 + b * 100 + c * 10 + d)
