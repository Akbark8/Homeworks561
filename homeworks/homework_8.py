import sqlite3


def create_tables(conn):
    cursor = conn.cursor()

    # Создаю таблицу жанров
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS genres (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE
        )
    ''')

    # Создаю таблицу книг с внешним ключом на genres
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            author TEXT,
            publication_year INTEGER,
            number_of_pages INTEGER,
            number_of_copies INTEGER,
            genre_id INTEGER,
            FOREIGN KEY (genre_id) REFERENCES genres(id)
        )
    ''')

    conn.commit()
    print("Таблицы 'books' и 'genres' успешно созданы.")


def insert_genres(conn):
    genres = [
        ("Роман",),
        ("Фантастика",),
        ("Фэнтези",),
        ("Притча",),
    ]
    cursor = conn.cursor()
    cursor.executemany("INSERT OR IGNORE INTO genres (name) VALUES (?)", genres)
    conn.commit()
    print(f"Добавлено жанров: {len(genres)}")


def insert_books(conn):
    # Получаю жанры из базы, чтобы взять их id
    cursor = conn.cursor()
    cursor.execute("SELECT id, name FROM genres")
    genre_map = {name: gid for gid, name in cursor.fetchall()}

    books = [
        ("Война и мир", "Лев Толстой", 1869, 1225, 5, genre_map["Роман"]),
        ("1984", "Джордж Оруэлл", 1949, 328, 7, genre_map["Фантастика"]),
        ("Гарри Поттер", "Джоан Роулинг", 1997, 320, 10, genre_map["Фэнтези"]),
        ("Маленький принц", "Антуан Экзюпери", 1943, 96, 8, genre_map["Притча"]),
        ("Анна Каренина", "Лев Толстой", 1877, 864, 6, genre_map["Роман"]),
    ]

    cursor.executemany('''
        INSERT INTO books (name, author, publication_year, number_of_pages, number_of_copies, genre_id)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', books)
    conn.commit()
    print(f"Добавлено книг: {len(books)}")


def select_books_with_genres(conn):
    """Выводит книги с жанрами (JOIN)"""
    cursor = conn.cursor()
    cursor.execute('''
        SELECT books.name, books.author, books.publication_year, genres.name
        FROM books
        JOIN genres ON books.genre_id = genres.id
    ''')

    results = cursor.fetchall()
    print("\nКниги и их жанры:")
    print("-" * 60)
    print(f"{'Название':<30} | {'Автор':<20} | {'Год':<4} | Жанр")
    print("-" * 60)
    for name, author, year, genre in results:
        print(f"{name:<30} | {author:<20} | {year:<4} | {genre}")


def main():
    conn = sqlite3.connect("library.db")
    print("Подключение к базе данных установлено.")

    try:
        create_tables(conn)
        insert_genres(conn)
        insert_books(conn)
        select_books_with_genres(conn)
    finally:
        conn.close()
        print("\nСоединение с базой данных закрыто.")


if __name__ == "__main__":
    main()


