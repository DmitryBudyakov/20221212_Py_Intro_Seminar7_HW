def export_to_txt_file(contacts: list, filename: str):
    """ экспорт всех контактов в txt файл
    """
    with open(filename, 'w', encoding='utf8') as file:
        for contact in contacts:
            contact_lst = contact.split(',')
            file.write(' '.join(contact_lst))
    print('Экспорт в txt формат завершен.')
