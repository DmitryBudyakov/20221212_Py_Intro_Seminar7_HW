import model
import view
import logger

def phonebook_run():
    while True:
        view.cls_show_app_head()
        selector = view.phonebook_top_menu(top_menu, top_menu_choice, top_menu_actions)
        if selector == '1':     # поиск контакта
            view.cls_show_app_head()
            view.show_sub_menu(sub_menu_search)
            searched_contact = view.search_contact()
            print('Найденные контакты:')
            view.show_contact_head(contact_head)
            all_contacts = logger.read_from_file(pb_db_file)
            model.print_found_contact(all_contacts, searched_contact)
            print()
            input(msg_back_top_menu)
        elif selector == '2':   # добавление контакта
            view.cls_show_app_head()
            view.show_sub_menu(sub_menu_add_contact)
            print(msg_existing_contacts)
            view.show_contact_head(contact_head)
            all_contacts = logger.read_from_file(pb_db_file)
            model.print_contacts_with_tabs(all_contacts)
            print()
            added_contact = view.update_contact()
            updated_contacts = model.add_new_contact(all_contacts, added_contact)
            sorted_list = model.sort_contacts(updated_contacts)
            logger.write_to_file(sorted_list, pb_db_file, 1)
            view.cls_show_app_head()
            view.show_sub_menu(sub_menu_add_contact)
            print(msg_after_add)
            view.show_contact_head(contact_head)
            model.print_contacts_with_tabs(sorted_list)
            print()
            input(msg_back_top_menu)
        elif selector == '3':   # вывод всех контактов
            view.cls_show_app_head()
            view.show_sub_menu(sub_menu_show_contacts)
            print(msg_existing_contacts)
            view.show_contact_head(contact_head)
            all_contacts = logger.read_from_file(pb_db_file)
            model.print_contacts_with_tabs(all_contacts)
            print()
            input(msg_back_top_menu)
        elif selector == '4':   # изменение контакта
            view.cls_show_app_head()
            view.show_sub_menu(sub_menu_modify_contact)
            view.show_contact_head(contact_head)
            all_contacts = logger.read_from_file(pb_db_file)
            model.print_contacts_with_tabs(all_contacts)
            print()
            contact_id_to_modify = view.get_contact_id(msg_to_modify)
            modified_contact = view.update_contact()
            modified_contacts_sorted = model.sort_contacts(model.modify_contact(all_contacts, modified_contact, contact_id_to_modify))
            logger.write_to_file(modified_contacts_sorted, pb_db_file, 1)
            view.cls_show_app_head()
            view.show_sub_menu(sub_menu_modify_contact)
            print(msg_after_modify)
            view.show_contact_head(contact_head)
            model.print_contacts_with_tabs(modified_contacts_sorted)
            print()
            input(msg_back_top_menu)
        elif selector == '5':   # удаление контакта
            view.cls_show_app_head()
            view.show_sub_menu(sub_menu_del_contact)
            print(msg_existing_contacts)
            view.show_contact_head(contact_head)
            all_contacts = logger.read_from_file(pb_db_file)
            model.print_contacts_with_tabs(all_contacts)
            print()
            contact_to_del = view.get_contact_id(msg_to_delete)
            contacts_after_del = model.delete_contact(all_contacts, contact_to_del)
            logger.write_to_file(contacts_after_del, pb_db_file, 1)
            view.cls_show_app_head()
            view.show_sub_menu(sub_menu_del_contact)
            print(msg_after_del)
            view.show_contact_head(contact_head)
            model.print_contacts_with_tabs(contacts_after_del)
            print()
            input(msg_back_top_menu)
        elif selector == '6':   # экспорт контактов
            view.cls_show_app_head()
            view.show_sub_menu(sub_menu_export_book)
            all_contacts = logger.read_from_file(pb_db_file)
            logger.write_to_file(all_contacts, pb_txt_file, 2)
            print()
            input(msg_back_top_menu)


global msg_back_top_menu

pb_db_file = 'phonebook/phonebook.csv'
pb_txt_file = 'phonebook/phonebook.txt'

msg_back_top_menu = 'Нажмите [Enter] чтобы вернуться в Главное меню: '
msg_to_delete = 'Введите номер удаляемого контакта: '
msg_to_modify = 'Введите номер изменяемого контакта: '
msg_existing_contacts = 'Список существующих контактов:\n'
msg_after_del = 'Список контактов после удаления:\n'
msg_after_modify = 'Список контактов после изменения:\n'
msg_after_add = 'Список контактов после добавления:\n'

sub_menu_search = '1. Найти контакт\n'
sub_menu_add_contact = '2. Добавить контакт\n'
sub_menu_show_contacts = '3. Показать все контакты\n'
sub_menu_modify_contact = '4. Изменить контакт\n'
sub_menu_del_contact = '5. Удалить контакт\n'
sub_menu_export_book = '6. Экспорт контактов\n'
menu_item_exit = 'q. Выйти\n'
top_menu = 'Главное меню:\n'\
    + sub_menu_search\
    + sub_menu_add_contact\
    + sub_menu_show_contacts\
    + sub_menu_modify_contact\
    + sub_menu_del_contact\
    + sub_menu_export_book\
    + menu_item_exit
top_menu_choice = "Выбрать действие [1-6,q]: "
top_menu_actions = ['1','2','3','4','5','6','q']

contact_head = \
"No.\tФАМИЛИЯ\t\tИМЯ\t\tОТЧЕСТВО\t\tТЕЛЕФОН\n\
---\t-------\t\t---\t\t--------\t\t-------"
