from flask import Flask, render_template

app = Flask(__name__)

class User():
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def info(self):
        return '我叫哈哈哈33333哈'
@app.route('/index')
def test():
    name = {'name': 'hanjiping'}
    user = User('11',22)
    return render_template('index01.html', name=name ,user = user)




if __name__ == "__main__":
    app.run(debug=True)
