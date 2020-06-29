import sys
from os.path import abspath
from os.path import dirname

sys.path.insert(0, abspath(dirname(__file__)))

import app

'''
gunicorn 需要使用application 这个变量来启动flask

'''

application = app.app