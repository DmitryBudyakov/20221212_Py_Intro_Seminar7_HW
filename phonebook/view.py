import os

def clear_screen():
    """ очистка экрана """
    if os.name == 'nt':
        os.system('cls')
    else:
        clr_screen = os.system('clear')

def app_head():
    """ заголовок программы """
    title = 'Телефонная книга'
    title_line = '-'*len(title)
    head = f'{title_line}\n{title}\n{title_line}'
    print(head)


def phonebook_top_menu() -> str:
    """ меню телфонного справочника """
    menu_top_head =\
"Главное меню:\n\
1. Найти контакт\n\
2. Добавить контакт\n\
3. Показать все контакты\n\
4. Экспорт контактов\n\
q. Выйти\n"
    menu_top_choice = "Выбрать действие [1-4,q]: "
    pb_menu = menu_top_head + menu_top_choice
    actions = ['1','2','3','4','q']
    while True:
        action = input(pb_menu)
        if action not in actions:
            error_msg = 'Ошибка ввода. Повторите ввод.\n'
            pb_menu = menu_top_head + error_msg + menu_top_choice
            clear_screen()
            app_head()
        elif action == 'q':
            print(msg_on_exit)
            exit()
        else:
            return action

def view_init():
    clear_screen()
    app_head()
    phonebook_top_menu()

def phonebook_search_menu():
    """ Меню поиска контакта
    """
    menu_search_head = \
"Меню:\n\
1. Найти контакт\n"
# \n"
    clear_screen()
    app_head()
    print(menu_search_head)

def search_contact() -> str:
    search_string = input('Введите фамилию для поиска: ')
    return search_string
    
def show_contact_head():
    """ заголовок справочника """
    contact_head = \
"ФАМИЛИЯ\t\tИМЯ\t\tОТЧЕСТВО\t\tТЕЛЕФОН\n\
-------\t\t---\t\t--------\t\t-------"
    print(contact_head)

def phonebook_add_menu():
    """ Меню добавления контакта
    """
    menu_add_head = \
"Меню:\n\
2. Добавить контакт\n"
    clear_screen()
    app_head()
    print(menu_add_head)

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

def phonebook_all_contacts_menu():
    """ Меню показать все контакты
    """
    menu_all_cont_head = \
"Меню:\n\
3. Показать все контакты\n"
    clear_screen()
    app_head()
    print(menu_all_cont_head)

def phonebook_export_contacts_menu():
    """ Меню экспорта контактов
    """
    menu_export_cont_head = \
"Меню:\n\
4. Экспорт контактов\n\
   (--- в формат txt ---)\n"
    clear_screen()
    app_head()
    print(menu_export_cont_head)


global msg_on_exit        
msg_on_exit = 'Выход из справочника. Пока!'
