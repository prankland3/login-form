from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3
import hashlib


def register(username, password, password_repeat, email, firstName, lastName):
    if password == "" or password_repeat == "" or email == "" or firstName == "" or lastName == "":
        empty_err = "Some of the criteria isn't filled in please check them."
        return print(empty_err)
    elif password != password_repeat:
        repeat_err = "Password didn't match. Please try again."
        return print(repeat_err)
    elif len(password) < 8:
        password_len_err = "Password must be at least 8 characters long."
        return render_template("register.html"), password_len_err
    elif not any(char.islower() for char in password):
        password_lower_err = "Password must contain lower case letters."
        return render_template("register.html"), print(password_lower_err)
    elif not any(char.isupper() for char in password):
        password_upper_err = "Password must contain upper case letters."
        return render_template("register.html"), print(password_upper_err)
    elif not any(char.isdigit() for char in password):
        password_number_err = "Password must contain numbers."
        return render_template("register.html"), print(password_number_err)
    else:
        password = hashlib.md5(password.encode()).hexdigest()
        insert_user(username, password, email, firstName, lastName)
        success_sign_up = "sign up is successful.<br> you can now try to login"
        return render_template("login.html"), print(success_sign_up)


def insert_user(username, password, email, firstName, lastName):
    with sqlite3.connect("../database.db") as conn:
        cur = conn.cursor()
        cur.execute("""
        INSERT INTO users (
        firstname, 
        lastname, 
        email, 
        password, 
        username) 
        VALUES 
        (?, ?, ?, ?, ?)
        """, (firstName, lastName, email, password, username))
        conn.commit()
        cur.close()
