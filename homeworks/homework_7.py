import sqlite3


def create_table(conn):
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            name TEXT,
            author TEXT,
            publication_year INTEGER,
            genre TEXT,
            number_of_pages INTEGER,
            number_of_copies INTEGER
        )
    ''')
    conn.commit()
    print("Таблица books создана")


def insert_books(conn):
    books = [
        ("Война и мир", "Лев Толстой", 1869, "Роман", 1225, 5),
        ("Преступление и наказание", "Фёдор Достоевский", 1866, "Роман", 671, 3),
        ("1984", "Джордж Оруэлл", 1949, "Антиутопия", 328, 7),
        ("1984", "Джордж Оруэлл", 1949, "Антиутопия", 328, 7),  # случайно дублируется
        ("Мастер и Маргарита", "Михаил Булгаков", 1967, "Фантастика", 384, 4),
        ("Гарри Поттер", "Джоан Роулинг", 1997, "Фэнтези", 320, 10),
        ("Три товарища", "Эрих М. Ремарк", 1936, "Роман", 496, 2),
        ("Маленький принц", "Антуан Экзюпери", 1943, "Притча", 96, 8),
        ("Анна Каренина", "Лев Толстой", 1877, "Роман", 864, 6),
        ("Собачье сердце", "М. Булгаков", 1925, "Повесть", 192, 3),
    ]

    cursor = conn.cursor()
    cursor.executemany('''
        INSERT INTO books (name, author, publication_year, genre, number_of_pages, number_of_copies)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', books)
    conn.commit()
    print("Книги добавлены")


def select_books(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books")
    rows = cursor.fetchall()

    print("\nСписок книг:")
    print("------------------------------------------")
    for row in rows:
        print(row)


def main():
    conn = sqlite3.connect("library.db")
    print("База данных открыта")

    try:
        create_table(conn)
        insert_books(conn)
        select_books(conn)
    finally:
        conn.close()
        print("База данных закрыта")


if __name__ == "__main__":
    main()
