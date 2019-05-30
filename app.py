from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/index.html')
def index_page():
    return render_template('index.html')


@app.route('/base.html')
def base_page():
    return render_template('base.html', name='bootstrap')


if __name__ == '__main__':
    app.run()
