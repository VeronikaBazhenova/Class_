main_menu = ['Главное меню',
             'Открыть файл',
             'Сохранить файл',
             'Показать контакты',
             'Создать контакт',
             'Найти контакт',
             'Изменить контакт',
             'Удалить контакт',
             'Выход']
input_choice = 'Веберите пункт меню: '
input_error = f'Введённое число должно быть от 0 до {len(main_menu)-1}'

file_load = 'Телефонная книга загружена'
file_save = 'Телефонная книга сохранена'

empty_phone_book = 'Телефонная книга пуста'

new_contact = ['Введите имя', 'Введите номер телефона', 'Введите комнетарий']
confirm_changes = 'Сохранить контакт?'

for_search = 'Введите ключевое слово для поиска: '
for_edit = 'Введите ключевое слово для изменяемого контакта: '
input_edit_id = 'Введите ID изменяемого контакта'

input_edit_contact = ['Введите новое имя или оставьте пустым: '
                      'Введите новый номер телефона или оставьте пустым: '
                      'Введите новый коментарий или оставьте пустым: ' ]

for_del = 'Введите ключевое слово для удаляемого контакта: '
input_del_id = 'Введите ID удаляемого контакта'

end_program = 'До свидания!'

def contact_save_ok(name:str, operation):
    return f'Контакт {name} успешно {operation}'

def not_search(word: str) -> str:
    return f'Контакты, содержащие "{word} не найдены'


