text = input("Shifrlangan xabarni kiriting: ")  

left = " "
right = " "
flag = True

for symbol in text:
    if flag:
        left += symbol
        #print(left)
    else:
        right = symbol + right
        #print(right)
    flag = not flag

print("Shifrsizlangan xabar:", left + right)