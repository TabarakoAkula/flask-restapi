import flask
from flask.json import dumps
from flask import jsonify, request
from data import db_session
from data.users import User

blueprint = flask.Blueprint(
    'users_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/users')
def get_jobs():
    db_session.global_init('db/blogs.db')
    db_sess = db_session.create_session()
    users = db_sess.query(User).all()
    db_sess.close()
    return dumps(
        {
            'users':
                [item.to_dict(only=('id', 'name',
                                    'about', 'email',
                                    'hashed_password', 'created_date'))
                 for item in users]
        }
    )


@blueprint.route('/api/users/<int:works_id>', methods=['GET'])
def get_one_job(works_id):
    db_session.global_init('db/blogs.db')
    db_sess = db_session.create_session()
    users = db_sess.query(User).get(works_id)
    if not users:
        return dumps({'error': 'Not found'})
    db_sess.close()
    return dumps(
        {
            'works': users.to_dict(only=('id', 'name',
                                    'about', 'email',
                                    'hashed_password', 'created_date'))
        }, indent=4)


@blueprint.route('/api/users', methods=['POST'])
def create_works():
    if not request.json:
        return dumps({'error': 'Empty request'}, indent=4)
    elif not all(key in request.json for key in
                 ['id', 'name', 'about', 'email', 'hashed_password']):
        return dumps({'error': 'Bad request'}, indent=4)
    db_session.global_init('db/blogs.db')
    db_sess = db_session.create_session()
    if db_sess.query(User).get(request.json['id']):
        return dumps({'error': 'Already exists'}, indent=4)
    db_sess.add(User(
        id=request.json['id'],
        name=request.json['name'],
        about=request.json['about'],
        email=request.json['email'],
        hashed_password=request.json['hashed_password'],
        ))
    db_sess.commit()
    db_sess.close()
    return dumps({'success': 'OK'}, indent=4)


@blueprint.route('/api/users/<int:users_id>', methods=['DELETE'])
def delete_news(users_id):
    db_session.global_init('db/blogs.db')
    db_sess = db_session.create_session()
    users = db_sess.query(User).get(users_id)
    if not users:
        return dumps({'error': 'Not found'})
    db_sess.delete(users)
    db_sess.commit()
    db_sess.close()
    return dumps({'success': 'OK'})


@blueprint.route('/api/users/<int:users_id>', methods=['PUT'])
def edit_news(users_id):
    db_session.global_init('db/blogs.db')
    db_sess = db_session.create_session()
    users = db_sess.query(User).get(users_id)
    if not users:
        return dumps({'error': 'Not found'})
    if not request.json:
        return dumps({'error': 'Empty request'}, indent=4)
    elif not all(key in request.json for key in
                 ['name', 'about', 'email', 'hashed_password']):
        return dumps({'error': 'Bad request'}, indent=4)
    users.name = request.json['name']
    users.about = request.json['about']
    users.email = request.json['email']
    users.hashed_password = request.json['hashed_password']
    db_sess.commit()
    db_sess.close()
    return dumps({'success': 'OK'})