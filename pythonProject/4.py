#Отсортировать словарь my_dict = {'a':50, 'c':5, 'd': 56,'e':4, 'f':58,
#'z': 20} по ключу в порядке возрастания. Вывести на экран первые три элемента.

my_dict = {'a': 50, 'c': 5, 'd': 56, 'e': 4, 'f': 58, 'z': 20}
sorted_keys = sorted(my_dict.keys())
first_three_keys = sorted_keys[:3]
print("Первые три элемента отсортированного словаря:")
for key in first_three_keys:
    print(key, ":", my_dict[key])