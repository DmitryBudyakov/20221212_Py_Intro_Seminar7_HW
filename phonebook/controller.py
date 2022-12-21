import model
import view
import logger

def phonebook_run():
    while True:
        view.clear_screen()
        view.app_head()
        selector = view.phonebook_top_menu()
        if selector == '1':     # поиск контакта
            view.clear_screen()
            view.app_head()
            view.phonebook_search_menu()
            searched_contact = view.search_contact()
            print('Найденные контакты:')
            view.show_contact_head()
            all_contacts = model.read_from_file(pb_db_file)
            model.print_found_contact(all_contacts, searched_contact)
            print()
            input('Нажмите [Enter] чтобы вернуться в Главное меню: ')
        elif selector == '2':   # добавление контакта
            view.clear_screen()
            view.app_head()
            view.phonebook_add_menu()
            added_contact = view.add_contact()
            model.write_to_db_file(added_contact, pb_db_file)
            print()
            input('Нажмите [Enter] чтобы вернуться в Главное меню: ')
        elif selector == '3':   # вывод всех контактов
            view.clear_screen()
            view.app_head()
            view.phonebook_all_contacts_menu()
            view.show_contact_head()
            model.print_contacts_with_tabs(model.read_from_file(pb_db_file))
            print()
            input('Нажмите [Enter] чтобы вернуться в Главное меню: ')
        elif selector == '4':   # экспорт контактов
            view.clear_screen()
            view.app_head()
            view.phonebook_export_contacts_menu()
            all_contacts = model.read_from_file(pb_db_file)
            logger.export_to_txt_file(all_contacts, pb_txt_file)
            print()
            input('Нажмите [Enter] чтобы вернуться в Главное меню: ')

pb_db_file = 'phonebook/phonebook.csv'
pb_txt_file = 'phonebook/phonebook.txt'    