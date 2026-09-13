import pytest

from books import get_book, get_shelf, add_book


books = [
    {
        'number': 'P-1234',
        'title': 'Евгений Онегин',
        'author': 'Александр Пушкин'
    },
    {
        'number': 'F-88006',
        'title': 'Властелин колец',
        'author': 'Джон Р. Р. Толкин'
    },
    {
        'number': 'D-1122',
        'title': 'Безмолвный свидетель',
        'author': 'Агата Кристи'
    }
]


directories = {
    '1': ['P-1234', 'F-88006'],
    '2': ['D-1122'],
    '3': []
}


@pytest.mark.parametrize(
    "book_number, expected",
    [
        ("P-1234", "Книга: Евгений Онегин\nАвтор: Александр Пушкин"),
        ("D-1122", "Книга: Безмолвный свидетель\nАвтор: Агата Кристи"),
        ("12345", "Книга не найдена в базе"),
    ]
)
def test_get_book(book_number, expected):
    assert get_book(books, book_number) == expected


@pytest.mark.parametrize(
    "book_number, expected",
    [
        ("P-1234", "1"),
        ("D-1122", "2"),
        ("12345", "Полки с такой книгой не найдено"),
    ]
)
def test_get_shelf(book_number, expected):
    assert get_shelf(directories, book_number) == expected


def test_add_existing_book():
    result = add_book(
        books,
        directories,
        "P-1234",
        "Евгений Онегин",
        "Александр Пушкин",
        "3"
    )

    assert result == "Такая книга уже есть в списке"


def test_add_new_book():
    test_books = books.copy()
    test_directories = {
        key: value.copy()
        for key, value in directories.items()
    }

    result = add_book(
        test_books,
        test_directories,
        "N-5678",
        "Война и мир",
        "Лев Толстой",
        "3"
    )

    assert result == "Книга добавлена на полку: 3"
    assert test_books[-1]["number"] == "N-5678"
    assert "N-5678" in test_directories["3"]