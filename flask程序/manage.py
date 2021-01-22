import flask

from flask import Flask, render_template

app = Flask(__name__)
app.debug = True


class User():
    def __init__(self,username,age):
        self.username = username
        self.age = age

    def get_info(self):
        return f"我的名字是{self.username},我的年龄{self.age}"


@app.route('/index')
def index():
    name = {'name': '11'}
    list_number = [i for i in range(10)]
    user = User('韩',18)
    return render_template('index.html', name=name, number=list_number,user = user)


@app.route('/user/<username>')
def user_name_info(username):
    return render_template('name.html', name=username)


@app.route('/login', methods=['POST', 'GET'])
def login():
    return 'get'


if __name__ == "__main__":
    app.run()
