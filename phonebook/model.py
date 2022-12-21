def write_to_db_file(contact: list, filename: str):
    """ запись нового контакта в базу
    """
    with open(filename, 'a', encoding='utf8') as file:
        file.write(','.join(contact) + '\n')
        
def read_from_file(filename: str) -> list:
    """ Чтение записей из файла """
    with open(filename, 'r', encoding='utf8') as file:
        lines = file.readlines()
    return lines

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
    