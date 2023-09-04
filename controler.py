import text
import view
import modul


def search_block(msg: str):
    request = view.input_request(msg)
    result = modul.search(request)
    view.show_book(result, text.not_search((request)))
    if result:
        return True


def start():
    while True:
        choice = view.menu()
        match choice:
            case 1:
                modul.open_file()
                view.print_msg(text.file_load)
            case 2:
                modul.save_file()
                view.print_msg(text.file_save)
            case 3:
                book = modul.phone_book
                view.show_book(book, text.empty_phone_book)
            case 4:
                contact = view.input_contact(text.input_edit_contact)
                modul.add_contact(contact)
                view.print_msg(text.contact_save_ok(contact[0], 'сохранён'))
            case 5:
                search_block(text.for_search)
            case 6:
                if search_block(text.for_edit):
                    edit_id = int(view.input_request(text.input_edit_id))
                    new_contact = view.input_contact(text.input_edit_contact)
                    modul.edit(edit_id, new_contact)
                    view.print_msg(text.contact_save_ok(new_contact[0], 'изменён'))
            case 7:
                if search_block(text.for_del):
                    del_id = int(view.input_request(text.input_del_id))
                    name = modul.del_contact(del_id)[0]
                    view.print_msg(text.contact_save_ok(name, 'удалён'))
            case 8:
                view.print_msg(text.end_program)
                break
