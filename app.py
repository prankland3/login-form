from flask import Flask, render_template, url_for, redirect, request, session

from auth import register
from auth import login

app = Flask(__name__)


@app.route('/')
def home():  # put application's code here
    return render_template('index.html', )

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
        password = data["password"]
        password_repeat = data["passwordRepeat"]
        email = data["email"]
        firstName = data["firstName"]
        lastName = data["lastName"]
        return register.register(username, password, password_repeat, email, firstName, lastName)
    else:
        return render_template("register.html")



if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)
