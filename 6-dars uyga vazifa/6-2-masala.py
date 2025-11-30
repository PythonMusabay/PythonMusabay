name = input('Ismni kiriting: ')
debt = int(input('Qarz miqdorini kiriting: '))
print(name, "sizning qarzingiz", debt, 'rublni tashkil qiladi')
pay = int(input("Qarzni to'lash uchun siz hozir qancha kiritasiz? "))
while debt >= pay:
    print("Bu kam", name, 'yana qoshing.')
    pay = int(input("Qarzni to'lash uchun siz hozir qancha kiritasiz? "))
print("Juda yaxshi, Baxodir! Siz qarzingizni to'ladingiz. Rahmat!")