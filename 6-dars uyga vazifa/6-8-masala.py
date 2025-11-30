bags = int(input("Nechta qopni tashish kerak: "))
total_weight = 0
bags_count = 0
while bags_count <= bags:
    weight = int(input("Qop og'irligi necha kilo? "))
    total_weight += weight
    bags_count += 1
    print("Qoplar tashildi ", bags_count, bags, "dan")

print("Qoplarning umumiy og'irligi, ", total_weight)

# bu masalada da xatolik bor shunga yordam bera olasizmi