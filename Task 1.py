# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

x = [2, 3, 5, 9, 3,]
summ = 0
for i in range(1, len(x), 2):
        summ += x[i]       
print(f"{x} -> Ответ: {summ}")