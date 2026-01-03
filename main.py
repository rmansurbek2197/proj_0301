# 1
ism = input("Ismingizni kiriting: ")
print(f"Salom, {ism}! Python dunyosiga xush kelibsiz!")


# 2
tugilgan_yil = int(input("Tug‘ilgan yilingizni kiriting: "))
yosh = 2026 - tugilgan_yil
print(f"Siz {yosh} yoshdasiz.")


# 3
son = int(input("Biror raqam kiriting: "))

if son % 2 == 0:
    print("Bu raqam juft.")
else:
    print("Bu raqam toq.")


# 4
a = int(input("1-raqamni kiriting: "))
b = int(input("2-raqamni kiriting: "))
c = int(input("3-raqamni kiriting: "))

eng_katta = max(a, b, c)
print("Eng katta raqam:", eng_katta)


# 5
print("1 - Selsiydan Farengeytga")
print("2 - Farengeytdan Selsiyga")

tanlov = int(input("Tanlovingizni kiriting (1 yoki 2): "))

if tanlov == 1:
    c = float(input("Selsiy darajani kiriting: "))
    f = (c * 9/5) + 32
    print(f"{c}°C = {f}°F")

elif tanlov == 2:
    f = float(input("Farengeyt darajani kiriting: "))
    c = (f - 32) * 5/9
    print(f"{f}°F = {c}°C")

else:
    print("Noto‘g‘ri tanlov!")
