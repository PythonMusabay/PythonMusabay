boys = int(input("O'g'il bolalar sonini kiriting: "))
girls = int(input("Qizlar sonini kiriting: "))

answer = " "
if (boys > 2 * girls) or (girls > boys * 2):
    print("Yechim yo'q")
elif boys >= girls:
    k = boys - girls
    for bgb in range(k):
        answer += "BGB"
    for gb in range(girls - k):
        answer += "GB"
else:
    k = girls - boys
    for gbg in range(k):
        answer += "GBG"
    for bg in range(boys - k):
        answer += "BG"

print(answer)