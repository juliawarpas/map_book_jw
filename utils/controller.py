def get_user_info(users_data: list) -> None:
    for user in users_data:
        print(f'Twój znajomy {user['name']} z miejscowości {user['location']} opublikował {user["posts"]}')


def add_user(users_data: list) -> None:
    new_name: str = input('Podaj imię nowego znajomego: ')
    new_location: str = input('Podaj nazwe lokalizacji: ')
    new_posts: int = int(input('Podaj liczbę postów: '))
    users_data.append({'name': new_name, 'location': new_location, 'posts': new_posts}, )


def remove_user(users_data: list) -> None:
    user_name: str = input('Wpisz kogo chcesz usunąć: ')
    for user in users_data:
        if user['name'] == user_name:
            users_data.remove(user)


def update_user(users_data: list) -> None:
    user_name: str = input('Wpisz kogo chcesz zmodyfikować: ')
    for user in users_data:
        if user['name'] == user_name:
            user['name'] = input('Podaj nowe imię: ')
            user['location'] = input('Podaj nową lokalizację: ')
            user['posts'] = input('Podaj liczbę postów: ')
