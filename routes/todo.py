from flask import (
    Blueprint,
    render_template,
)
from utils import log

main = Blueprint('todo', __name__)


@main.route('/', methods=["GET"])
def index():
    return '<h1>hello<h2>'
@main.route('/message')
def message():
    return 'ok niohao'

@main.route('/msg/<int:id>/')
def test(id):
    log(id)
    return f'传入的id为{id}'