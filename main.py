import json

# Заглушка для данных об играх
games = []


def display_games(games):
    if not games:
        print("Нет доступных игр.")
        return
    print("\nСписок игр:")
    for idx, game in enumerate(games, start=1):
        print(f"{idx}. Название: {game['title']}, Жанр: {game['genre']}, Год: {game['year']}")


def add_game():
    title = input("Введите название игры: ").strip()
    genre = input("Введите жанр игры: ").strip()
    year = input("Введите год выпуска игры: ").strip()

    if title and genre and year.isdigit():
        games.append({"title": title, "genre": genre, "year": int(year)})
        print(f"Игра '{title}' успешно добавлен.")
    else:
        print("Ошибка: Пожалуйста, введите корректные данные.")


def remove_game():
    display_games(games)
    try:
        index = int(input("Введите номер игры для удаления: ")) - 1
        if 0 <= index < len(games):
            removed_game = games.pop(index)
            print(f"Игра '{removed_game['title']}' успешно удален.")
        else:
            print("Ошибка: Неверный номер игры.")
    except ValueError:
        print("Ошибка: Пожалуйста, введите корректный номер.")


def search_game():
    keyword = input("Введите ключевое слово для поиска: ").strip().lower()
    found_games = list(filter(lambda m: keyword in m['title'].lower() or keyword in m['genre'].lower(), games))

    if found_games:
        display_games(found_games)
    else:
        print("Игры не найдены.")


def filter_games():
    genre_filter = input("Введите жанр для фильтрации (или оставьте пустым для всех): ").strip().lower()
    filtered_games = list(filter(lambda m: genre_filter in m['genre'].lower() if genre_filter else True, games))

    if filtered_games:
        display_games(filtered_games)
    else:
        print("Игры не найдены.")


def main_menu():
    while True:
        print("\nДобро пожаловать в систему управления магазина компьютерных игр!")
        print("Выберите действие:")
        print("1. Добавить игру")
        print("2. Удалить игру")
        print("3. Поиск игры")
        print("4. Фильтрация игр")
        print("5. Выход")

        choice = input("Ваш выбор: ")

        if choice == '1':
            add_game()
        elif choice == '2':
            remove_game()
        elif choice == '3':
            search_game()
        elif choice == '4':
            filter_games()
        elif choice == '5':
            print("Выход из программы.")
            break
        else:
            print("Ошибка: Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main_menu()
