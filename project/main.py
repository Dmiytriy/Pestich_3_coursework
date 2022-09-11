
from flask import Flask, render_template

from project.bookmarks.bookmarks_views import bookmarks_blueprint
from project.posts.posts_views import posts_blueprint
from project.api.utils import api_blueprint

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

# Регистрация блюпринтов
app.register_blueprint(posts_blueprint)
app.register_blueprint(api_blueprint)
app.register_blueprint(bookmarks_blueprint)


# Считывание ошибок
@app.errorhandler(404)
def handle_bad_request():
    return render_template('404.html')


@app.errorhandler(500)
def handle_bad_request(error):
    return render_template('500.html')


if __name__ == "__main__":
    app.run()
