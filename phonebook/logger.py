def write_to_file(contacts: list, filename: str, filetype: int):
    """ Запись контактов в файл
        filetype: 1 - csv, 2 - txt
    """
    with open(filename, 'w', encoding='utf-8') as file:
        for contact in contacts:
            contact_lst = contact.split(',')
            if filetype == 1:
                file.write(','.join(contact_lst))
            elif filetype == 2:
                file.write(' '.join(contact_lst))
    if filetype == 2:
        print('Экспорт в txt формат завершен.')
    
def read_from_file(filename: str) -> list:
    """ Чтение записей из файла """
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    return lines

