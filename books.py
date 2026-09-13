def get_book(books, book_number):  # передаём каталог книг и номер книги в качестве аргументов функции
    # итерируемся по элементам списка books
    for book in books:
        # получаем каждый номер книги по ключу и сравниваем с переданным
        if book['number'] == book_number:
            return f"Книга: {book['title']}\nАвтор: {book['author']}"  # возвращаем требуемые значения по ключу
    return "Книга не найдена в базе"


def get_shelf(directories, book_number):  # передаём аргументы в функцию
    # итерируемся по ключам и значениям directories
    for shelf, books in directories.items():
        # проверяем наличие искомого номера в значениях словаря
        if book_number in books:
            return shelf  # возвращаем номер полки
    # если совпадений нет, возвращаем "Полки с такой книгой не найдено"
    return "Полки с такой книгой не найдено"


def add_book(books, directories, number, title, author, shelf):  # передаём аргументы в функцию
    # проходим в цикле по всем полкам (значениям) словаря directories
    for books_numbers in directories.values():
        # проверяем, есть ли уже такой номер книги на текущей полке
        if number in books_numbers:
            return "Такая книга уже есть в списке"

    # формируем словарь с данными, которые потом добавятся к списку книг
    new_book = {
        "number": number,
        "title": title,
        "author": author
    }
    books.append(new_book)  # добавляем словарь к списку

    # проверяем, что переданный номер полки существует среди ключей directories
    if shelf in directories:
        # добавляем номер книги к списку по найденному ключу-номеру полки
        directories[shelf].append(number)
    else:
        # создаём новую полку с новым номером и добавляем туда номер книги
        directories[shelf] = [number]
    return f"Книга добавлена на полку: {shelf}"


if __name__ == '__main__':
    books = [
        {'number': 'P-1234', 'title': 'Евгений Онегин', 'author': 'Александр Пушкин'},
        {'number': 'F-88006', 'title': 'Властелин колец', 'author': 'Джон Р. Р. Толкин'},
        {'number': 'D-1122', 'title': 'Безмолвный свидетель', 'author': 'Агата Кристи'}
    ]

    directories = {
        '1': ['P-1234', 'F-88006'],
        '2': ['D-1122'],
        '3': []
    }

    print(get_book(books, "P-1234"))
    print(get_shelf(directories, "D-1122"))
    print(get_book(books, "12345"))
    print(add_book(books, directories, 'P-1234', 'Евгений Онегин', 'Александр Пушкин', '3'))
    print(add_book(books, directories, 'N-5678', 'Война и мир', 'Лев Толстой', '3'))
    print(get_shelf(directories, "N-5678"))
    print(get_book(books, "N-5678"))
    print(get_shelf(directories, "12345"))