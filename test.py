from requests import post, get, delete, put


def test():
    print('Get')
    print()
    print(get('http://localhost:5000/api/jobs').json())
    print()
    print(get('http://localhost:5000/api/jobs/1').json())
    print()
    print(get('http://localhost:5000/api/jobs/999').json())
    print()
    print(get('http://localhost:5000/api/jobs/q1xcvds').json())
    print()
    print()
    ''' все работы одна работа несуществующая работа ошибочное значение '''
    print('Post')
    print()
    print()
    print(post('http://localhost:5000/api/jobs',
               json={'id': 4, 'team_leader': 'Boss', 'title_of_activity': 'test', 'work_size': 21,
                     'collaborators': '1, 2, 3', 'is_finished': True}).json())
    print(get('http://localhost:5000/api/jobs').json())
    print()
    print(post('http://localhost:5000/api/jobs', json={}).json())
    print()
    print(post('http://localhost:5000/api/jobs', json={'id': '4'}).json())
    print()
    print(post('http://localhost:5000/api/jobs', json={'news': 'woo'}).json())
    print()
    print()
    ''' правильный запрос пустой неправильный формат данных несуществующее значение '''
    print('Delete')
    print()
    print()
    print(post('http://localhost:5000/api/jobs',
               json={'id': 5, 'team_leader': 'Boss', 'title_of_activity': 'test', 'work_size': 21,
                     'collaborators': '1, 2, 3', 'is_finished': True}).json())
    print(delete('http://localhost:5000/api/jobs/5').json())
    print()
    print(delete('http://localhost:5000/api/jobs/555').json())
    print()
    print(delete('http://localhost:5000/api/jobs/sss').json())
    ''' правильный + проверка не существует неправильный тип данных '''
    print()
    print()
    print('Put')
    print()
    print()
    print(put('http://localhost:5000/api/jobs/3',
              json={'title_of_activity': 'changed', 'collaborators': '1, 2', "team_leader": 'changed_leader',
                    'is_finished': False, 'work_size': 12}).json())
    print()
    print(put('http://localhost:5000/api/jobs/3', json={}).json())
    print()
    print(put('http://localhost:5000/api/jobs/99', json={'title_of_activity': 'changed'}).json())
    print()
    print()
    print('Users_Api')
    print()
    print()
    print(get('http://localhost:5000/api/users').json())
    print()
    print(get('http://localhost:5000/api/users/2').json())

    print(post('http://localhost:5000/api/users', json={'id': 4,
                                                        'name': 'Users_Put',
                                                        "about": 'USers_Put_About',
                                                        'email': 'mm@mail.ru',
                                                        'hashed_password': 'sdfgsdfgfdsds'}).json())
    print()
    print(put('http://localhost:5000/api/users/4', json={'name': 'edUsers_Put',
                                                         "about": 'ChangedUSers_Put_About',
                                                         'email': 'changed_mm@mail.ru',
                                                         'hashed_password': 'sdfgsdfgfdsds'}).json())
    print(delete('http://localhost:5000/api/users/4').json())


if __name__ == '__main__':
    test()
