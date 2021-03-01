#Преобразовать элементы списка s из строковой в числовую форму
def spisok_to_int(a):
    new_a = [int(item) for item in a]
    return new_a

#Подсчитать количество различных элементов в последовательности s
def count(a):
    quantity = len(set(a))
    return quantity

#Обратить последовательность s без использования функций
def razv(a):
    new_a = a[::-1]
    return new_a

#Выдать список индексов, на которых найден элемент x в последовательности s
def index(a):
    new_a = [i for i, j in enumerate(a) if j == '0']
    return new_a

#Сложить элементы списка s с четными индексами
def summa(a):
    summ = sum([j for i, j in enumerate(a) if i % 2 == 0])
    return summ

#Найти строку максимальной длины в списке строк s
def maxx(a):
    max_len = max([len(i) for i in a])
    return max_len

#Тест №1
print(spisok_to_int(['5', '6', '7', '0']))

#Тест №2
print(count(['5', '6', '7', '0', '0']))

#Тест №3
print(razv(['5', '6', '7', '0']))

#Тест №4
print(index(['5', '6', '7', '0', '0']))

#Тест №5
print(summa([5, 6, 7, 0, 4]))

#Тест №6
print(maxx(['5', '6666', 'Brraaa', '033', 'w4']))

