def print_contacts_with_tabs(lines: list):
    line_num = 0
    for line in lines:
        line_num += 1
        cont_num = f'{line_num}.\t'
        entries = line[:-1].split(',')
        print(cont_num + '\t\t'.join(entries))

def print_found_contact(contacts: list, to_find: str):
    count = 0
    for entry in contacts:
        if to_find.lower() in entry.lower():
            count += 1
            cont_num = f'{count}.\t'
            contact_lst = entry[:-1].split(',')
            print(cont_num + '\t\t'.join(contact_lst))
    if count == 0:
        print(f"Контакты по фильтру '{to_find}' не найдены.")

def add_new_contact(contacts: list, contact: list) -> list:
    """ Добавление контакта к списку контактов """
    new_contact = f"{','.join(contact)}\n"
    contacts.append(new_contact)
    return contacts

def sort_contacts(contacts: list) -> list:
    """ Сортировка списка контактов """
    sorted_list = sorted(contacts)
    return sorted_list

def delete_contact(contacts: list, contact_num: int) -> list:
    """ Удаление контакта """
    del(contacts[contact_num-1])
    return contacts