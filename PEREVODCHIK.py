from tkinter import *
import tkinter.font as font
import random
from PIL import Image, ImageTk


# Функции для кнопок
def test_btn_click():
    menu.pack_forget()
    module.pack()


# Функция для открытия переводчика
def perev_btn_click():
    global r
    menu.pack_forget()
    perevodchik.pack()


# Функция для запуска переворотного квадрата
def m_btns_click(event):
    global whatmod, r
    whatmod = int(event.widget['text'][-1]) - 1
    r = random.randint(0, len(fverbs[whatmod]) - 1)
    module.pack_forget()
    card_btn.config(text=fverbs[whatmod][r])
    all_about_verb_widget["text"] = '[' + fdeffinitions[whatmod][r] + '] ' + fexamples[whatmod][r]
    test.pack()


# Функция для кнопки возврата из модулей, окна с тестовой карточкой
def back(event):
    test.pack_forget()
    module.pack()


# Функция кнопки возврата из режима переводчика
def mainmenu_back_fromperev_func(event):
    perevodchik.pack_forget()
    menu.pack()


# Функция для выхода из меню выбора модуля в главное меню
def mainmenu_back_func(event):
    module.pack_forget()
    menu.pack()


# Функция для кнопки следующего глагола
def next(event):
    global whatmod, r, language
    if language is True:
        r = random.randint(0, len(fverbs[whatmod]) - 1)
        card_btn["text"] = fverbs[whatmod][r]
        all_about_verb_widget["text"] = '[' + str(fdeffinitions[whatmod][r]) + '] ' + str(fexamples[whatmod][r])

    else:
        r = random.randint(0, len(ftranslation[whatmod]) - 1)
        card_btn["text"] = ftranslation[whatmod][r]


# Функция для перевода с обратной стороны карточки
def card_btn_click():
    global r, module
    global language
    if language is True:
        card_btn.config(text=ftranslation[whatmod][r])
        all_about_verb_widget["text"] = ''
        language = False
    else:
        card_btn.config(text=fverbs[whatmod][r])
        all_about_verb_widget["text"] = '[' + fdeffinitions[whatmod][r] + '] ' + fexamples[whatmod][r]
        language = True


# Функция при которой текст внутри поисковой строки исчезнет
def search_visible(event):
    perevodchik_search.configure(state=NORMAL)
    perevodchik_search.delete(0, END)


# Функция для возврата значени введите глагол в поисковой строке, если там пустота
def search_invisible(event):
    if perevodchik_search.get() == '':
        perevodchik_search.insert(0, "Введите глагол")
        perevodchik_search.configure(state=DISABLED)


# Функция для лупы, поиска информации для глагола
def lupa_search_verb(event):
    lupa_word_search = perevodchik_search.get()
    if lupa_word_search != 'Введите глагол' and lupa_word_search != '':
        if lupa_word_search != '':
            lupa_word_search = lupa_word_search[0].upper() + lupa_word_search[1:].lower()
        try:
            searching_word_ind = verbs.index(lupa_word_search)
            all_about_perevod_widget["text"] = translations[searching_word_ind] + "\n" + "\n" + "Ex.: " + examples[
                searching_word_ind] + "\n" + "\n" + "Def.: " + deffinitons[searching_word_ind]
        except:
            all_about_perevod_widget['text'] = "Слово не найдено"


# Функция для открытия окна справки
def help_click(event):
    window_help = Toplevel()
    window_help.iconbitmap("helpicon.ico")
    window_help.resizable(width=False, height=False)
    window_help.geometry('300x250')
    window_help.title("Справка")
    window_help.configure(bg='#4484f7')
    # Лэйбл и канвас для нового окна, в котором справка сама прописана
    spravka_canv = Canvas(window_help, width=300, height=250, bg='#4484f7', )
    spravka_canv.pack(padx=(10,10),pady=(10,10))
    # Скроллбар, чтобы листать текст
    helpscroll = Scrollbar(window_help, orient="vertical")
    helpscroll.pack(side=RIGHT, fill="y")

    help = Text(spravka_canv, bg='#4484f7',font=authorFont,fg="white",  yscrollcommand= helpscroll.set, wrap= WORD)
    help.insert(END, 'Тренажер и переводчик фразовых глаголов английского языка  — это приложение '
                                   'автоматического перевода фразовых глаголов английского языка с учебника по '
                                   'Английскому языку за 10 класс: Баранова К.М. Starlight 10. '
                                   'С дополнительным режимом тренажера для запоминания английских слов.\n \n' 
    'Приложения использует технологию машинного перевода, основанную на встроенной базее данных. \n \n'
    'Режим "Тестирование" - режим позволяющий пользователю заучивать фразовые глаголы по системе карточек. '
    'Вы можете выбрать один из 5 моулей, составленных по учебнику. Для того, чтобы увидеть перевод глагола, '
    'необходимо нажать на карточку. Для перехода к следующему глаголу нужно нажать кнопку "Next".\n \n'
    'Режим "Переводчик" - режим позволяющий пользователю находить нужный фразовый глагол при помощи поисковой '
                           'строки. Для нахождения перевода слова нажмите на надпись "Введите глагол", затем введите '
                           'нужный глагол и нажмите кнопку "Enter" или на икоку лупы. Если ввыеденный глагол '
                           'отсутствует в базе данных, то на экран выведится надпись "Слово не найдено".')
    helpscroll.config(command=help.yview())
    help.config(state=DISABLED)

    help.pack()
    window_help.grab_set()


    #spravka_canv.pack()



# Кусок из старого кода для работы модулей и выдачи рандомного глагола, все переменные
f = open('verbs.txt', 'r', encoding='utf-8')
list = f.readlines()
verbs = []
deffinitons = []
examples = []
translations = []
language = True
rand = random.randint(0, len(list) - 2)  # как только вводим строчку со словом модуль, отнимаем 1 т.е -1
modules = [0, 0, 0, 0, 0]  # сколько модулей, столько и нулей -- модулей 5
number = 0  # кол-во слов в модуле (фразовых глаголов в модуле) -- счётчик
for i in range(1, len(list)):
    if 'Модуль' not in list[i]:
        verbs.append(list[i][:list[i].find(' =')])
        deffinitons.append(list[i][list[i].find('=') + 2:list[i].find(';')])
        examples.append(list[i][list[i].find(';') + 2:list[i].rfind('.')])
        translations.append(list[i][list[i].rfind('.') + 2:-1])
        modules[number] += 1
    else:
        number += 1

fverbs = []
fdeffinitions = []
fexamples = []
ftranslation = []
# Вложенные списки для каждого глагола, преревода, деффиниции и тп
lens = 0
for i in range(5):
    fverbs.append([])
    fdeffinitions.append([])
    fexamples.append([])
    ftranslation.append([])
    for j in range(modules[i]):
        fverbs[i].append(verbs[j + lens])
        fdeffinitions[i].append(deffinitons[j + lens])
        fexamples[i].append(examples[j + lens])
        ftranslation[i].append(translations[j + lens])

    lens += modules[i]

# Основа
window = Tk()
window.resizable(width=False, height=False)
window.geometry('500x450')
window.title("Тренажер")
window.iconbitmap("pcicon.ico")

# Перевод размеров кнопок в пиксели
pixelVirtual = PhotoImage(width=1, height=1)

# Создание канвас, страниц, основной канвас, с которого все начинается
menu = Canvas(window, width=500, height=450, bg="#4484f7")

# Шрифты
buttonFont = font.Font(size=16, family="Open Sans")
authorFont = font.Font(size=10, family="Open Sans")
cardFont = font.Font(size=16, family="Open Sans")
all_about_Font = font.Font(size=12, family="Open Sans")

# Первые две кнопки первой страницы
test_btn = Button(menu, text='Тестирование', width=180, height=120, font=buttonFont, command=test_btn_click,
                  image=pixelVirtual, compound='center')
trans_btn = Button(menu, text="Переводчик", width=180, height=120, font=buttonFont, command=perev_btn_click,
                   image=pixelVirtual, compound='center')  # Сделал сам
test_btn.place(x=40, y=150)
trans_btn.place(x=270, y=150)

# Надписи(лейблы)первой страницы
name = Label(menu, text="Выберите режим", font=buttonFont, bg="#4484f7", fg="white")
name.place(x=160, y=90)
author = Label(menu, text="Создано: Алексеенко А" + "\n 2023" , font=authorFont, bg="#4484f7", fg="white")
author.place(x=300, y=380)
menu.pack()

# Лэйбл для справки
help = Label(menu, text="Справка", font=authorFont, bg="#4484f7", fg="white", cursor="fleur")
help.bind('<Button-1>', help_click)
help.place(x=50, y=380)




# Канвас для выбора модуля
module = Canvas(window, width=500, height=450, bg='#4484f7')
m1_btn = Button(module, text='Модуль 1', width=200, height=40, font=cardFont, image=pixelVirtual, compound='center')
m1_btn.bind('<Button-1>', m_btns_click)
m1_btn.place(x=150, y=85)
m2_btn = Button(module, text='Модуль 2', width=200, height=40, font=cardFont, image=pixelVirtual, compound='center')
m2_btn.bind('<Button-1>', m_btns_click)
m2_btn.place(x=150, y=145)
m3_btn = Button(module, text='Модуль 3', width=200, height=40, font=cardFont, image=pixelVirtual, compound='center')
m3_btn.bind('<Button-1>', m_btns_click)
m3_btn.place(x=150, y=205)
m4_btn = Button(module, text='Модуль 4', width=200, height=40, font=cardFont, image=pixelVirtual, compound='center')
m4_btn.bind('<Button-1>', m_btns_click)
m4_btn.place(x=150, y=265)
m5_btn = Button(module, text='Модуль 5', width=200, height=40, font=cardFont, image=pixelVirtual, compound='center')
m5_btn.bind('<Button-1>', m_btns_click)
m5_btn.place(x=150, y=325)

# Канвас 1 для раздела переводчика
perevodchik = Canvas(window, width=500, height=450, bg="#4484f7")  # Тоже сам сделал
perevodchik.bind('<Button-1>', search_invisible)

# Поисковая строка в переводчике
perevodchik_search = Entry(perevodchik, width=20, font=cardFont)
perevodchik_search.place(x=70, y=80)  # было 140 по оси y
perevodchik_search.bind('<Button-1>', search_visible)
perevodchik_search.bind("<Return>", lupa_search_verb)

# Текст внутри поисковой строки
perevodchik_search.insert(0, "Введите глагол")
perevodchik_search.configure(state=DISABLED)

# Канвас 2 - тест, вторая стр
test = Canvas(window, width=500, height=450, bg="#4484f7")

# Стрелка картинка из меню с переворотной карточкой в меню модулей
strelka_back = ImageTk.PhotoImage(Image.open('strelka.png'))
strelka_back_widget = Label(test, image=strelka_back, bg="#4484f7")
strelka_back_widget.bind('<Button-1>', back)
strelka_back_widget.place(x=10, y=10)

# Лэйбл для лупы
lupa = ImageTk.PhotoImage(Image.open('lupa.png'))
lupa_search = Label(perevodchik, image=lupa, bg="#4484f7")
lupa_search.bind('<Button-1>', lupa_search_verb)
lupa_search.place(x=400, y=70)

# Лэйбл для текста выдаваемого при вводе в строку переводчика
all_about_perevod_widget = Label(perevodchik, text='', font=all_about_Font, bg="#4484f7", wraplength=400,
                                 compound="center", width=45, fg="white")
all_about_perevod_widget.bind('<Button-1>')
all_about_perevod_widget.place(x=50, y=150)

# Кнопка переворотная с глаголом
card_btn = Button(test, text='', width=320, height=150, font=cardFont, image=pixelVirtual, command=card_btn_click,
                  compound='center', wraplength=300)
card_btn.place(x=90, y=50)

# Лэйбл для примера, транскрипции и дефениции при перевороте карточки
all_about_verb_widget = Label(test, text='', font=all_about_Font, bg="#4484f7", wraplength=400, compound="center",
                              fg="white")
all_about_verb_widget.bind('<Button-1>')
all_about_verb_widget.place(x=60, y=220)

# Кнопка назад
back_btn = Button(test, text='BACK', width=40, height=20, font=authorFont, image=pixelVirtual, compound='center',
                  command=back, bg="#4484f7")

# Кнопка возврата из меню модулей на основной экран тест
mainmenu_back = ImageTk.PhotoImage(Image.open('strelka.png'))
mainmenu_back_widget = Label(module, image=strelka_back, bg="#4484f7")
mainmenu_back_widget.bind('<Button-1>', mainmenu_back_func)
mainmenu_back_widget.place(x=10, y=10)

# Кнопка возврата из меню переводичка
mainmenu_back_fromperev = ImageTk.PhotoImage(Image.open('strelka.png'))
mainmenu_back_fromperev_widget = Label(perevodchik, image=strelka_back, bg="#4484f7")
mainmenu_back_fromperev_widget.bind('<Button-1>', mainmenu_back_fromperev_func)
mainmenu_back_fromperev_widget.place(x=10, y=10)

# Стрелка для следующего глагола Кнопка NEXT
nextword_btn = Button(test, text='NEXT', width=40, height=150, font=authorFont, image=pixelVirtual, compound='center')
nextword_btn.bind('<Button-1>', next)
nextword_btn.place(x=440, y=50)

res = []
for i in range(len(translations)):
    print((translations[i]))

for i in range(len(verbs)):
    if "Stand" in verbs:
        print(i)


window.mainloop()

# найти спрайт стрелки пнг для кнопки назад
# Переделать код, чтобы работали модули(переворотная карточка)
# по оси х - 500, по У - 350
