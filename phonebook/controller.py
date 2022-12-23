import model
import view
import logger

def phonebook_run():
    while True:
        view.cls_show_app_head()
        selector = view.phonebook_top_menu(top_menu)
        if selector == '1':     # поиск контакта
            view.cls_show_app_head()
            view.show_sub_menu(sub_menu_search)
            searched_contact = view.search_contact()
            print('Найденные контакты:')
            view.show_contact_head()
            all_contacts = model.read_from_file(pb_db_file)
            model.print_found_contact(all_contacts, searched_contact)
            print()
            input('Нажмите [Enter] чтобы вернуться в Главное меню: ')
        elif selector == '2':   # добавление контакта
            view.cls_show_app_head()
            view.show_sub_menu(sub_menu_add_contact)
            added_contact = view.add_contact()
            model.write_to_db_file(added_contact, pb_db_file)
            print()
            input('Нажмите [Enter] чтобы вернуться в Главное меню: ')
        elif selector == '3':   # вывод всех контактов
            view.cls_show_app_head()
            view.show_sub_menu(sub_menu_show_contacts)
            view.show_contact_head()
            model.print_contacts_with_tabs(model.read_from_file(pb_db_file))
            print()
            input('Нажмите [Enter] чтобы вернуться в Главное меню: ')
        elif selector == '4':   # экспорт контактов
            view.cls_show_app_head()
            view.show_sub_menu(sub_menu_export_book)
            all_contacts = model.read_from_file(pb_db_file)
            logger.export_to_txt_file(all_contacts, pb_txt_file)
            print()
            input('Нажмите [Enter] чтобы вернуться в Главное меню: ')

pb_db_file = 'phonebook/phonebook.csv'
pb_txt_file = 'phonebook/phonebook.txt'
sub_menu_search = '1. Найти контакт\n'
sub_menu_add_contact = '2. Добавить контакт\n'
sub_menu_show_contacts = '3. Показать все контакты\n'
sub_menu_export_book = '4. Экспорт контактов\n'
menu_item_exit = 'q. Выйти\n'
top_menu = sub_menu_search + sub_menu_add_contact + sub_menu_show_contacts + sub_menu_export_book + menu_item_exit
