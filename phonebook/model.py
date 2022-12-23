def print_contacts_with_tabs(lines: list):
    for line in lines:
        entries = line[:-1].split(',')
        print('\t\t'.join(entries))

def print_found_contact(contacts: list, to_find: str):
    count = 0
    for entry in contacts:
        if to_find.lower() in entry.lower():
            count += 1
            contact_lst = entry[:-1].split(',')
            print('\t\t'.join(contact_lst))
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
