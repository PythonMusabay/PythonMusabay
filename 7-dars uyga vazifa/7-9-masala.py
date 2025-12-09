number = True
salary = int(input('Ish haqin kiriting: '))

for month in range(9):
    prev_salary = salary
    salary = int(input('Ish haqin kiriting: '))
    if prev_salary >= salary:
        number = False

if number:
    print('Ish haqi har oyda oshib boryapti')
else:
    print('Ish haqi beqaror')
