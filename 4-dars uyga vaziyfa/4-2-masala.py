text_russian = int(input("Rus tili bo'yicha ballar miqdorini kiriting: "))
text_math = int(input("Matematika bo'yicha ballar miqdorini kiriting: "))
text_infor = int(input("Informatika bo'yicha ballar miqdorini kiriting: "))
if (text_russian + text_math + text_infor) >= 270:
    print("Tabriklaymiz, siz byudjet asosida qabul qilindingiz!")
else:
    print("Afsuski, siz byudjet asosida qabul qilinmadingiz!")