def remove_empty_columns(table):
    for i in range(len(table)):
        for j in range(len(table[0])):
            for k in range(table[i].count(None)):
                table[i].remove(None)
    return table


def remove_double_rows(table):
    new_table = list()
    for row in table:
        if row not in new_table and set(row) != {None}:
            new_table.append(row)
    return new_table


def transform(new_table):
    for i in range(len(new_table)):
        for j in range(len(new_table[0])):
            if j == 0:
                new_table[i][j] = new_table[i][j].replace('.', '-')
            if j == 1:
                new_table[i][j] = new_table[i][j].replace('да', 'Да')
                new_table[i][j] = new_table[i][j].replace('нет', 'Нет')
            if j == 2:
                new_table[i][j] = new_table[i][j][:new_table[i][j].index('@')]
    return new_table


def main(table):
    return transform(remove_double_rows(remove_empty_columns(table)))


input_1 = [['25.02.00', 'да', None, 'cezskij49@mail.ru'],
           ['18.11.02', 'нет', None, 'serskij63@gmail.com'],
           ['18.11.02', 'нет', None, 'serskij63@gmail.com'],
           ['18.11.02', 'нет', None, 'serskij63@gmail.com'],
           ['24.09.02', 'да', None, 'rorko52@rambler.ru'],
           ['11.08.01', 'нет', None, 'fadan4@yandex.ru']]

print(main(input_1))
