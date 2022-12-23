import os

def clear_screen():
    """ очистка экрана """
    if os.name == 'nt':
        os.system('cls')
    else:
        clr_screen = os.system('clear')

def app_head():
    """ заголовок программы """
    title = 'Телефонный аправочник'
    title_line = '-'*len(title)
    head = f'{title_line}\n{title}\n{title_line}'
    print(head)

def cls_show_app_head():
    clear_screen()
    app_head()

def phonebook_top_menu(menu_top_head: str) -> str:
    """ меню телфонного справочника """
    menu_top_choice = "Выбрать действие [1-4,q]: "
    pb_menu = menu_top_head + menu_top_choice
    actions = ['1','2','3','4','q']
    while True:
        action = input(pb_menu)
        if action not in actions:
            pb_menu = menu_top_head + error_msg_select + menu_top_choice
            cls_show_app_head()
        elif action == 'q':
            print(msg_on_exit)
            exit()
        else:
            return action
        
def show_sub_menu(title: str):
    """ Показывает подменю """
    menu_title = f'Меню:\n{title}'
    cls_show_app_head()
    print(menu_title)
    
def search_contact() -> str:
    search_string = input('Введите данные для поиска: ')
    return search_string
    
def show_contact_head():
    """ заголовок справочника """
    contact_head = \
"ФАМИЛИЯ\t\tИМЯ\t\tОТЧЕСТВО\t\tТЕЛЕФОН\n\
-------\t\t---\t\t--------\t\t-------"
    print(contact_head)

def add_contact() -> list:
    """ Добавление контакта
        Возвращает список с данными добавляемого контакта
    """
    contact_new = []
    family_name = input('Фамилия\t\t: ')
    first_name = input('Имя\t\t: ')
    second_name = input('Отчество\t: ')
    phone_number = input('Номер телефона\t: ')
    contact_new.append(family_name)
    contact_new.append(first_name)
    contact_new.append(second_name)
    contact_new.append(phone_number)
    return contact_new


global msg_on_exit, error_msg       
msg_on_exit = 'Выход из справочника. Пока!'
error_msg_select = 'Ошибка ввода. Повторите ввод.\n'
