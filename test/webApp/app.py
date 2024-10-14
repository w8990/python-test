from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "this is your first Python web server!"

if __name__ == '__main__':
    # 让应用运行在所有可用IP地址上，0.0.0.0表示监听所有公网/本地网IP
    app.run(host='0.0.0.0', port=5000)
