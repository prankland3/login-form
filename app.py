from flask import Flask, render_template, url_for, redirect, request, session

from auth import register as reg
from auth import login

app = Flask(__name__, static_url_path='/static')


@app.route('/')
def home():  # put application's code here
    return render_template('index.html', title='Home')

@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        data = request.form
        username = data["userName"]
        password = data["password"]

        return login.login(username, password)
    else:
        return render_template("login.html")

@app.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':
        data = request.form
        username = data["userName"]
        password = data["pwd"]
        password_repeat = data["pwdRepeat"]
        email = data["email"]
        firstName = data["FirstName"]
        lastName = data["SecondName"]
        return reg.register(username, password, password_repeat, email, firstName, lastName)
    else:
        return render_template("register.html")

    print(register())



if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)
