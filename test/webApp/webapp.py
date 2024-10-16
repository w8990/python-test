from flask import Flask

# 定义 Flask 实例
flask_app = Flask(__name__)

@flask_app.route('/')
def home():
    return "Hello, this is your Flask web app running on Waitress!"

if __name__ == '__main__':
    from waitress import serve
    serve(flask_app, host='0.0.0.0', port=5000)
