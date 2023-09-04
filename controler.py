import text
import view
from modul import PhoneBook


def search_block(book: PhoneBook, msg: str):
    request = view.input_request(msg)
    result = book.search(request)
    view.show_book(result, text.not_search((request)))
    if result:
        return True


def start():
    pb = PhoneBook()
    while True:
        choice = view.menu()
        match choice:
            case 1:
                pb.open_file()
                view.print_msg(text.file_load)
            case 2:
                pb.save_file()
                view.print_msg(text.file_save)
            case 3:
                book = pb.phone_book
                view.show_book(book, text.empty_phone_book)
            case 4:
                contact = view.input_contact(text.input_edit_contact)
                pb.add_contact(contact)
                view.print_msg(text.contact_save_ok(contact[0], 'сохранён'))
            case 5:
                search_block(pb, text.for_search)
            case 6:
                if search_block(pb, text.for_edit):
                    edit_id = int(view.input_request(text.input_edit_id))
                    new_contact = view.input_contact(text.input_edit_contact)
                    pb.edit(edit_id, new_contact)
                    view.print_msg(text.contact_save_ok(new_contact[0], 'изменён'))
            case 7:
                if search_block(pb, text.for_del):
                    del_id = int(view.input_request(text.input_del_id))
                    name = pb.del_contact(del_id)[0]
                    view.print_msg(text.contact_save_ok(name, 'удалён'))
            case 8:
                if pb.phone_book != pb.original_book:
                    if view.input_request(text.confirm_changes).lower() == 'y':
                        pb.save_file()
                        view.print_msg(text.file_save)
                view.print_msg(text.end_program)
                break
