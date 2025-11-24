first_edu = int(input("O'qishga kirayotganlar ro'yxatidagi o'rinni kiriting: "))
num_ball = int(input("Imtihonlarda olgan ballar sonini kiriting: "))
if first_edu <= 10 and num_ball >= 290:
    print("Tabriklaymiz, Siz o'qishga kirdingiz!")
    print("Bonus sifatida sizga stipendiya hisoblab beriladi")
elif first_edu <= 10 and num_ball < 290:
    print("Tabriklaymiz, Siz o'qishga kirdingiz!")
    print("Lekin stipendiya olish uchun sizda ballar yetishmadi")
else:
    print("Siz o'qishga kira olmadingiz!")