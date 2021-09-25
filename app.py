from flask import Flask
import config

app = Flask(__name__)
app.secret_key = config.secret_key

@app.route("/")
def hello():
    return "test my first flask app"

print("haha")

if __name__ == '__main__':
    config = dict(
        debug=True,
        host='0.0.0.0',
        port=5200,
    )
    app.run(**config)