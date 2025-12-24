

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/projectsapp/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'


def hello():
    return "Hello!"

app.add_url_rule(
    rule='/',
    endpoint="hello1",       # default would be 'hello' anyway
    view_func=hello,
    methods=["GET"]
)


if __name__ == '__main__':
    app.run(debug=True)



