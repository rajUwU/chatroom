from flask import Flask, url_for,request, render_template
from markupsafe import Markup

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p> Hello, World</p>"

@app.route("/lmao")
def lmao_page():
    return "<p> Hi this is the lmao page</p>"

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f'Post {post_id}'

@app.route('/path/<path:sub_path>')
def show_subpath(sub_path):
    return f'Subpath {sub_path}'

@app.route('/projects/')
def projects():
    return 'The project page'




@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

with app.test_request_context():
    print(url_for('hello_world'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))
    print(url_for('static', filename='style.css'))

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', person=name)






