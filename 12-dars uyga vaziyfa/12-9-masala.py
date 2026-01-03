def rock():
    word = input("tosh, qaychi, qog`oz so`zlarini tanlang: ")
    if word == 'tosh':
        print("Siz yutdingiz!!!")
    elif word == 'qaychi':
        print("Teng")
    elif word == 'qog`oz':
        print("Siz yutqazdingiz")
    else:
        print("Xato so`z kiritingiz")
    print("Asosiy menyuga qaytish")
    main_menu()

def number_f():
  number = int(input("Sonni kiriting : "))
  if number == 8:
    print("Siz raqamni topdingiz")
  elif number > 8:
    print("Soningiz katta")
    number_f()
  elif number < 8:
    print("Soningiz kichik")
    number_f()
  print("Asosiy menyuga qaytish")
  main_menu()
  
def main_menu():
  number = int(input("O'yinni tanlang 1 - tosh, qaychi, qogoz, 2 - raqamni top: "))
  if number == 1:
    rock()
  elif number == 2:
    number_f()
  else:
    print("Bunday oyin yoq")
  
main_menu()