from flask import Flask

from utils import log

from routes.todo import main as todo_routes


# 初始化
app = Flask(__name__)

# secret_key
app.secret_key = 'random str'

app.register_blueprint(todo_routes, url_prefix='/todo')



if __name__ == "__main__":
    config = dict(
        debug=True,
        port=2000,
        host='0.0.0.0'
    )
    app.run(**config)


