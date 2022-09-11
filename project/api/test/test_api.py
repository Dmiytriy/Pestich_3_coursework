import pytest


from project.main import app


def test_api_posts():
    """ Тест полностью"""
    response = app.test_client().get('/api/posts')
    data = response.json[0]
    assert response.status_code == 200, "Ошибка доступа"
    assert type(response.json) == list, "Неверный формат"
    assert data["poster_name"] == "leo", "Неверный ключ"


def test_api_post():
    """ Тест отдельного поста"""
    response = app.test_client().get('/api/posts/3')
    data = response.json
    assert response.status_code == 200, "Ошибка доступа"
    assert type(response.json) == dict, "Неверный формат"
    assert data["poster_name"] == "leo", "Неверный ключ"
