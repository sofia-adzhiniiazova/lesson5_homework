#1.Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

prog_file = input('Введите строки, которые необходимо записать в файл: ')
file = open(prog_file,'w')
while True:
    s = input()
    if s == '':
        break
    file.write(s+'\n')
file.close()


#2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке.

f = open('text2.txt')
line = 0
for i in f:
    line += 1
    flag = 0
    word = 0
    for j in i:
        if j != ' ' and flag == 0:
            word += 1
            flag = 1
        elif j == ' ':
            flag = 0
    print(i, len(i), 'символов', word, 'слов(а)')

print(line, 'строк')
f.close()


#3.Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

employers = {}
with open('employers_salary.txt', 'r', encoding='UTF-8') as file_3:
    for line in file_3:
        key, value = line.split()
        employers[key] = value
print('Сотрудники с окладом меньше 20000р.')
for i,j in employers.items():
    if float(j) < 20000:
        print(i, j)
print(f'Средняя зарплата сотрудников: {sum(map(float, employers.values())) / len(employers)}руб')


#4.Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.


rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_file = []
with open('text4.txt', 'r') as file_obj:
    for i in file_obj:
        i = i.split(' ', 1)
        new_file.append(rus[i[0]] + ' ' + i[1])
    print(new_file)

with open('file_4_new.txt', 'w') as file_obj_2:
    file_obj_2.writelines(new_file)


#5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.


from random import randint
with open('file_5.txt', 'w') as fifth_file:
    for i in range(10):
        fifth_file.write(f'{(randint(1, 20))} ')
with open('file_5.txt', 'r') as numbers:
    a = numbers.read().split()
    print(f'Числа из файла: {a}')
    print(f'Сумма произвольных чисел из файла равна {sum(map(int, a))}')


#6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
#практических и лабораторных занятий по этому предмету и их количество.
#Важно, чтобы для каждого предмета не обязательно были все типы занятий.
#Сформировать словарь, содержащий название предмета и общее количество занятий по нему.Вывести словарь на экран.
#Примеры строк файла:
#Информатика: 100(л) 50(пр) 20(лаб).
#Физика: 30(л) — 10(лаб)
#Физкультура: — 30(пр) —
#Пример словаря:
#{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

import re
dict_6 = {}
with open('file_6.txt', 'r', encoding='UTF-8-sig') as sixth_file:
    for i in sixth_file:
        key, *value = i.split()
        dict_6[key] = [re.match(r'(\d*)', j).group() for j in value]
for i, j in dict_6.items():
    value = [int(x) for x in j if x]
    dict_6[i] = sum(value)
print(dict_6)


#7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
#Пример строки файла: firm_1 ООО 10000 5000.
#Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
#Если фирма получила убытки, в расчет средней прибыли ее не включать.
#Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
#Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
#Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
#Итоговый список сохранить в виде json-объекта в соответствующий файл.
#Пример json-объекта:
#[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#Подсказка: использовать менеджеры контекста.

import json
seventh_dict1 = {}
seventh_dict2 = {}
average = {}
with open('file_7.txt', 'r', encoding='UTF-8-sig') as seventh_file:
    for i in seventh_file:
        key, *value = i.split()
        value = list(map(int, value[1:]))
        profit = value[0] - value[-1]
        seventh_dict2[key] = profit
        if profit > 0:
            seventh_dict1[key] = profit
    seventh_dict1['average_profit'] = sum(seventh_dict1.values())/len(seventh_dict1)
    average['average_profit'] = sum(seventh_dict2.values()) / len(seventh_dict2)
print(f'Выводим словарь по первому подзаданию: {seventh_dict1}')
print(f'Выводим список по второму подзаданию: {[seventh_dict2, average]}')
out_list = [seventh_dict2, average]
with open('seventh_output.json', 'w', encoding='UTF-8') as seventh_output:
    json.dump(out_list, seventh_output, ensure_ascii=False)