import os

def clear_screen():
    """ очистка экрана """
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def app_head():
    """ заголовок программы """
    title = 'Телефонный справочник'
    title_line = '-'*len(title)
    head = f'{title_line}\n{title}\n{title_line}'
    print(head)

def cls_show_app_head():
    """ Очистка экрана и вывод заголовка """
    clear_screen()
    app_head()

def phonebook_top_menu(menu_top_head: str, menu_top_choice: str, actions: list) -> str:
    """ Меню телефонного справочника """
    pb_menu = menu_top_head + menu_top_choice
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
    """ Запрос на поиск """
    search_string = input('Введите данные для поиска: ')
    return search_string
    
def show_contact_head(contact_head: str):
    """ Поля справочника """
    print(contact_head)

def update_contact() -> list:
    """ Добавление/Изменение контакта
        Возвращает список с данными добавляемого/изменяемого контакта
    """
    contact_upd = []
    family_name = input('Фамилия\t\t: ')
    first_name = input('Имя\t\t: ')
    second_name = input('Отчество\t: ')
    phone_number = input('Номер телефона\t: ')
    contact_upd.append(family_name)
    contact_upd.append(first_name)
    contact_upd.append(second_name)
    contact_upd.append(phone_number)
    return contact_upd

def get_contact_id(prompt: str) -> int:
    """ Возвращает No. контакта из списка """
    cont_number = int(input(prompt))
    return cont_number

global msg_on_exit, error_msg       
msg_on_exit = '\nВыход из справочника. Пока!\n'
error_msg_select = 'Ошибка ввода. Повторите ввод.\n'
