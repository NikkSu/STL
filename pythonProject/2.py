#2 Посчитать, сколько пар (стоят рядом) верхнего и нижнего
#регистра находится в веденном с клавиатуры слове. (Пример HjkLM- 1
#пара нижнего, 1 пара верхнего), а также сколько всего букв в слове.

while True:
    word = input("Введите слово: ")
    if word.isalpha():
        break
    else:
        print("Пожалуйста, введите только буквы.")
upper_pairs = 0
lower_pairs = 0
total_letters = 0
for i in range(len(word) - 1):
    if word[i].isupper() and word[i + 1].isupper():
        upper_pairs += 1
    elif word[i].islower() and word[i + 1].islower():
        lower_pairs += 1
total_letters = len(word)
print("Количество пар верхнего регистра:", upper_pairs)
print("Количество пар нижнего регистра:", lower_pairs)
print("Общее количество букв в слове:", total_letters)