import random

f = open('verbs.txt', 'r', encoding='utf-8')
list = f.readlines()
verbs = []
deffinitons = []
examples = []
translations = []
rand = random.randint(0, len(list) - 2)  # как только вводим строчку со словом модуль, отнимаем 1 т.е -1
module = [0, 0, 0, 0, 0]  # сколько модулей, столько и нулей -- модулей 5
number = 0  # кол-во слов в модуле (фразовых глаголов в модуле) -- счётчик
for i in range(1, len(list)):
    if 'Модуль' not in list[i]:
        verbs.append(list[i][:list[i].find(' =')])
        deffinitons.append(list[i][list[i].find('=') + 2:list[i].find(';')])
        examples.append(list[i][list[i].find(';') + 2:list[i].rfind('.')])
        translations.append(list[i][list[i].rfind('.') + 2:-1])
        module[number] += 1
    else:
        number += 1

while True:
    print("1 - Режим теста\n2 - Режим перевода")



    word = int(input())


    if word == 1:
        choise = int(input('Введите номер модуля. Если хотите выйти в меню, то нажмите 0 '))
        while str(choise) != "0":
            if choise == 1:
                rand = random.randint(0, module[0] - 1)
            elif choise == 2:
                rand = random.randint(module[0], module[0] + module[1] - 1)
            elif choise == 3:
                rand = random.randint(module[0] + module[1], module[0] + module[1] + module[2] - 1)
            elif choise == 4:
                rand = random.randint(module[0] + module[1] + module[2],
                                    module[0] + module[1] + module[2] + module[3] - 1)
            elif choise == 5:
                rand = random.randint(module[0] + module[1] + module[2] + module[3],
                                      module[0] + module[1] + module[2] + module[3] + module[4] - 1)
            else:
                print("Такого модуля не существует")
                break


            print(verbs[rand])  # module[0] + module[1], module[0]+ module[1]+ module [2] -1 когда элиф 3
            choise = input()
            print(deffinitons[rand])
            choise = input()
            print(translations[rand])
            choise = input()
            print(examples[rand])
            choise = input()
    elif word == 2:
        slovo = 1
        while slovo != "0":
            slovo = input("Введите слово на английском языке. Если хотите выйти в меню, то нажмите 0 ")
            try:
                print(translations[verbs.index(slovo)])
            except:
                print("Слово не найдено")
    else:
        print("Такого режима не существует")
