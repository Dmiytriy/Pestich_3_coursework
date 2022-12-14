
from flask import Blueprint, jsonify
from project.logs.logs import my_logger
from project.utils import open_json_read


api_blueprint = Blueprint('api_blueprint', __name__)
#Запуск логирования
logger_api = my_logger('api', 'logs/api.log')


@api_blueprint.route('/api/posts')
def api_posts():
    """ Вывод всех постов"""
    logger_api.info("All Api")
    file = 'data/posts.json'
    data = open_json_read(file)
    return jsonify(data)


@api_blueprint.route('/api/posts/<int:pk>')
def single_post(pk):
    """ Вывод поста по ПК """
    logger_api.info("Api with PK")
    file = 'data/posts.json'
    data = open_json_read(file)
    for post in data:
        if pk == post["pk"]:
            post = post
        return jsonify(post)
