import flask
from flask.json import dumps
from flask import jsonify, request
from data import db_session
from data.works import Works

blueprint = flask.Blueprint(
    'jobs_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/jobs')
def get_jobs():
    db_session.global_init('db/blogs.db')
    db_sess = db_session.create_session()
    works = db_sess.query(Works).all()
    db_sess.close()
    return dumps(
        {
            'jobs':
                [item.to_dict(only=('id', 'title_of_activity',
                                    'team_leader', 'work_size',
                                    'collaborators', 'is_finished'))
                 for item in works]
        }
    )


@blueprint.route('/api/jobs/<int:works_id>', methods=['GET'])
def get_one_job(works_id):
    db_session.global_init('db/blogs.db')
    db_sess = db_session.create_session()
    works = db_sess.query(Works).get(works_id)
    if not works:
        return dumps({'error': 'Not found'})
    db_sess.close()
    return dumps(
        {
            'works': works.to_dict(only=('id', 'title_of_activity',
                                         'team_leader', 'work_size',
                                         'collaborators', 'is_finished'))
        }, indent=4)


@blueprint.route('/api/jobs', methods=['POST'])
def create_works():
    if not request.json:
        return dumps({'error': 'Empty request'}, indent=4)
    elif not all(key in request.json for key in
                 ['id', 'title_of_activity', 'team_leader', 'work_size', 'collaborators', 'is_finished']):
        return dumps({'error': 'Bad request'}, indent=4)
    db_session.global_init('db/blogs.db')
    db_sess = db_session.create_session()
    if db_sess.query(Works).get(request.json['id']):
        return dumps({'error': 'Already exists'}, indent=4)
    db_sess.add(Works(
        id=request.json['id'],
        title_of_activity=request.json['title_of_activity'],
        team_leader=request.json['team_leader'],
        work_size=request.json['work_size'],
        collaborators=request.json['collaborators'],
        is_finished=request.json['is_finished']
        ))
    db_sess.commit()
    db_sess.close()
    return dumps({'success': 'OK'}, indent=4)


@blueprint.route('/api/jobs/<int:works_id>', methods=['DELETE'])
def delete_news(works_id):
    db_session.global_init('ab/blogs.db')
    db_sess = db_session.create_session()
    works = db_sess.query(Works).get(works_id)
    if not works:
        return dumps({'error': 'Not found'})
    db_sess.delete(works)
    db_sess.commit()
    db_sess.close()
    return dumps({'success': 'OK'})