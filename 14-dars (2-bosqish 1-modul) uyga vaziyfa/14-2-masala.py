print("Birinchi nuqtani kiriting")
x_1 = float(input('X: '))
y_1 = float(input('Y: '))
print("\nIkkinchi nuqtani kiriting")
x_2 = float(input('X: '))
y_2 = float(input('Y: '))

x_diff = x_1 - x_2
y_diff = y_1 - y_2
if x_1 != x_2 and y_1 != y_2:
    k = y_diff / x_diff
    b = y_2 - k * x_2
    print("Ushbu nuqtalar orqali o'tuvchi to'g'ri chiziq tenglamasi:")
    print("y = ", k, " * x + ", b)
elif  x_1 == x_2:
    print("x = ", x_1)
elif  y_1 == y_2:
    print("y = ", y_1)
