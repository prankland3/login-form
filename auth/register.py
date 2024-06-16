
from flask import render_template
import hashlib
from db.db import DatabaseConnection


def register(username, password, password_repeat, email, firstName, lastName):
    error_messages = []
 
    if password == "" or password_repeat == "" or email == "" or firstName == "" or lastName == "":
        empty_err = "Some of the criteria isn't filled in please check them."
        return render_template("register.html", err = empty_err)

    else:
        if password != password_repeat:
            repeat_err = "Password didn't match. Please try again."
            error_messages.append(repeat_err)

        if len(password) < 8:
            password_len_err = "Password must be at least 8 characters long."
            error_messages.append(password_len_err)

        if not any(char.islower() for char in password):
            password_lower_err = "Password must contain lower case letters."
            error_messages.append(password_lower_err)

        if not any(char.isupper() for char in password):
            password_upper_err = "Password must contain upper case letters."
            error_messages.append(password_upper_err)

        if not any(char.isdigit() for char in password):
            password_number_err = "Password must contain numbers."
            error_messages.append(password_number_err)

    if len(error_messages) == 0:
        password = hashlib.md5(password.encode()).hexdigest()
        insert_user(username, password, email, firstName, lastName)
        success_sign_up = "sign up is successful.\n you can now try to login"
        return render_template("login.html", err = success_sign_up)
    else:
        return render_template("register.html", err = error_messages)


def insert_user( username, password, email, firstName, lastName):
    try:
        with DatabaseConnection() as cur:
            cur.execute("""
                INSERT INTO users (firstname, lastname, email, password, username) 
                VALUES (%s, %s, %s, %s, %s)
                """, (firstName, lastName, email, password, username))
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
