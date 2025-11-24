first_num = int(input("Birinchi sonni kiriting: "))
second_num = int(input("Ikkinchi sonni kiriting: "))
third_num = int(input("Uchunchi sonni kiriting: "))
if (first_num > second_num and (second_num > third_num) and (first_num > third_num) or (first_num > second_num) and
        (second_num < third_num) and (first_num > third_num)):
    print("Birinchi son katta:", first_num)
elif (first_num < second_num) and (second_num >third_num):
    print("Ikkinchi son katta:",second_num)
else:
    print("Uchunchi son katta", third_num)


# Bu erda qisqa kod yozishning iloji bormi if shartida ko'payib ketti