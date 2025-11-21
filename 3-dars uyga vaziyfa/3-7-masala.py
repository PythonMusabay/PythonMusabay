# Bu erda v = s / t  formula bo'yicha harakatlanadi
v = int(input("Tezlikni kiriting: "))
t = int(input("Vaqtni kiriting: "))
s = 115
summ_1 = (v * t) // s
summ_2 = (v * t) % s 
print("Necha krug yugurgan", summ_1)
print("Aylananing nechanichi km da toqtagan:", summ_2)