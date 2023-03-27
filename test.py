from requests import post, get, delete, put


def test():

    print(post('http://localhost:5000/api/users', json={'id': 3,
                                                        'name': 'Users_Put',
                                                        "about": 'USers_Put_About',
                                                        'email': 'mm@mail.ru',
                                                        'hashed_password': 'sdfgsdfgfdsds'}).json())
    print()
    print(put('http://localhost:5000/api/users/3', json={'name': 'ChangedUsers_Put',
                                                         "about": 'USers_Put_About',
                                                         'email': 'changed_mm@mail.ru',
                                                         'hashed_password': 'sdfgsdfgfdsds'}).json())
    print()
    print(delete('http://localhost:5000/api/users/3').json())


if __name__ == '__main__':
    test()
