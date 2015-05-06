from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Zbys'}
    posts = [

        {
            'author': {'nickname': 'John'},
            'body': 'beauty day'
        },

        {
            'author': {'nickname': 'Suzan'},
            'body': 'avengers was so cool!'
        }

    ]

    return render_template('index.html', title='Home', user=user, posts=posts)


if __name__ == '__main__':
    app.run()
