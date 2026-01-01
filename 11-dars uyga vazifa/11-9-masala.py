import math
equation_a = float(input("Kvadarat tenglamaning a koeffitsentin kirirting: "))
equation_b = float(input("Kvadarat tenglamaning b koeffitsentin kirirting: "))
equation_c = float(input("Kvadarat tenglamaning c koeffitsentin kirirting: "))
equation_a != 0
discrim = equation_b ** 2 - 4 * equation_a * equation_c
if discrim > 0:
    print("Ikkita yechim:  x1 = ", (-equation_b - math.sqrt(discrim))/(2 * equation_a), "va  x2 = ", (-equation_b + math.sqrt(discrim))/(2 * equation_a))
elif discrim == 0:
    print("Bitta yechim:  x = ", (-equation_b)/(2 * equation_a))
else:
    print("Yechimi yo'q")
