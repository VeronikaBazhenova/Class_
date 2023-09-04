phone_book = {}
PATH = 'book.txt'


def open_file():
    global phone_book
    with open(PATH, 'r', encoding='UTF-8') as file:
        data = file.readlines()
    for i, contact in enumerate(data):
        contact = contact.strip().split(';')
        phone_book[i] = contact


def save_file():
    global phone_book
    data = []
    for contact in phone_book.values():
        data.append(';'.join([*contact]))
    with open(PATH, 'w', encoding='UTF-8') as file:
        file.write('\n'.join(data))


def add_contact(new: list[str]):
    global phone_book
    c_id = max(phone_book) + 1
    phone_book[c_id] = new


def search(word: str) -> dict[int, list[str]]:
    global phone_book
    result = {}
    for i, contact in phone_book.items():
        for file in contact:
            if word.lower() in file.lower():
                result[i] = contact
                break
    return result


def edit(c_id: int, contact: list[str]):
    global phone_book
    current_contact = phone_book.get(c_id)
    new_contact = [contact[i] if contact[i] else current_contact[0] for i in range(3)]

    phone_book[c_id] = new_contact


def del_contact(c_id: int) -> dict[int, list[str]]:
    global phone_book
    return phone_book.pop(c_id)