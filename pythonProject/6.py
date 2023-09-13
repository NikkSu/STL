#Дан кортеж целых чисел. Найти сумму элементов после первого положительного
numbers = input("Введите кортеж целых чисел через ПРОБЕЛ: ").split()
positive_found = False
sum_after_positive = 0
for num in numbers:
    if num.isdigit():
        num = int(num)
        if positive_found:
            sum_after_positive += num
        elif num > 0:
            positive_found = True
print("Сумма элементов после первого положительного числа:", sum_after_positive)