#1.Определить, сколько в числе четных цифр, а сколько нечетных. Число вводится с клавиатуры.
while True:
    try:
        number = int(input("Введите число: "))
        break
    except ValueError:
        print(" введите число заново.")
chet = 0
nchet = 0
digits = str(abs(number))
for digit in digits:
    if int(digit) % 2 == 0:
        chet += 1
    else:
        nchet += 1
print("Количество четных цифр:", chet)
print("Количество нечетных цифр:", nchet)