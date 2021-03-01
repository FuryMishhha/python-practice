import K1

def f23(table):
    table1 = []
    for i in table:
        if i not in table1:
            table1.append(i)
    table = table1

    #Преобразования (проценты)
    for i in range(len(table)):
        x = ''
        if (table[i][0][3] == '1' or table[i][0][3]=='4') and table[i][0][4]=='5':
            for j in range(0, len(table[i][0])-1):
                x += table[i][0][j]
            x += '4'
            table[i][0] = x
        elif table[i][0][4] == '5':
            for j in range(0, len(table[i][0])-1):
                x += table[i][0][j]
            x += '6'
            table[i][0] = x
        table[i][0] = '{:.0%}'.format(float(table[i][0]))

    #Преобразования (фамилия)
    for i in range(0, len(table)):
        sub = ''
        for j in range(0, len(table[i][1])-5):
            sub += table[i][1][j]
        table[i][1] = sub

    #Преобразования (email)
    for i in range(0, len(table)):
        x = 0
        sub = ''
        for j in range(0, len(table[i][2])):
            if table[i][2][j] != '@':
                sub += table1[i][2][j]
            else:
                x = j
                break
        sub += '[at]'
        for j in range(x+1, len(table[i][2])):
            sub += table[i][2][j]
        table[i][2] = sub

    #Транспонирование
    table2 = []
    for j in range (0, len(table1[0])):
        table2.append([])
        for i in range (0, len(table1)):
            table2[j].append(table1[i][j])
    table = table2

    return table

"""
print(f23([
    ['0.653', 'Шумиди М.Б.', 'sumidi43@yandex.ru'],
    ['0.015', 'Шеров А.У.', 'serov34@mail.ru'],
    ['0.276', 'Зодян Г.З.', 'zodan35@gmail.com'],
    ['0.276', 'Зодян Г.З.', 'zodan35@gmail.com'],
    ['0.276', 'Зодян Г.З.', 'zodan35@gmail.com'],
    ['0.170', 'Сизберг Э.Ц.', 'sizberg76@rambler.ru']
]))

print(f23([
    ['0.162', 'Нисибян М.У.', 'nisiban64@gmail.com'],
    ['0.716', 'Равесский М.Л.', 'ravesskij91@yandex.ru'],
    ['0.716', 'Равесский М.Л.', 'ravesskij91@yandex.ru'],
    ['0.716', 'Равесский М.Л.', 'ravesskij91@yandex.ru'],
    ['0.118', 'Сучовук Б.Ц.', 'sucovuk72@mail.ru']
]))
"""


for i in range(0, len(K1.tests['f23'][17])):
    print(i)
    print(K1.tests['f23'][17][i][0])
    print()
    print(f23(K1.tests['f23'][17][i][0]))
    print()
    print(K1.tests['f23'][17][i][1])
    print()

    #print(f23(K1.tests['f23'][17][i][0]) == K1.tests['f23'][17][i][1])
