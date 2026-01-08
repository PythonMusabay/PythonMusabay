word = input("So'zni kiriting: ")
palindrom_check = [ ]
if word == word[::-1]:
    palindrom_check.append("So'z palindrom")
else:
    palindrom_check.append("So'z palindrom emas")

print(palindrom_check)