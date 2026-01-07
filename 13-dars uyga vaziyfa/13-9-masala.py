money = float(input("Kredit summasini kiritish: "))
year = int(input("Necha yilga berilgan? "))
interest = int(input("Yillik necha fiz?  "))
first_year = 3
def credit(interest, year, money):
  interest /= 100
  K = (interest * (1 + interest) ** year) / ((1 + interest) ** year - 1)
  A = K * money
  for i in range(first_year):
    print("\n davr: ", i+1)
    print("Davr boshidagi qarz qoldig'i: ", round(money, 2))
    summ_interest = interest * money
    print("Foizlar to'landi: ", round(summ_interest,2))
    summ_debt = A - summ_interest
    money -= summ_debt
    print("Asosiy kredit to'landi: ",round(summ_debt,2))
  print("Qarz qoldig'i: ", money)
  return money

money = credit(interest,year, money)

new_year = int(input("Shartnoma necha yilga uzaytiriladi? "))
new_interest = int(input("Stavkani gacha oshirish: "))
new_year += year - 3
first_year = new_year

credit(new_interest, new_year, money)
