#3 Найдите произведение элементов списка с нечетными номерами.
#Найдите наибольший элемент списка, затем удалите его и выведите новый список.

numbers = []
while True:
    num = input("Введите число или введите 'q' для завершения ввода: ")
    if num == 'q':
        break
    try:
        num = int(num)
        numbers.append(num)
    except ValueError:
        print("  введите ЧИСЛО или 'q' для завершения ввода!")
if len(numbers) > 0:
    product_odd = 1
    for i in range(len(numbers)):
        if i % 2 != 0:
            product_odd *= numbers[i]
    print("список до удаления наибольшего элемента:", numbers)
    max_number = max(numbers)
    numbers.remove(max_number)
    print("Новый список после удаления наибольшего элемента:", numbers)
    print("Произведение элементов с нечетными индексами:", product_odd)
else:
    print("Список пуст.")