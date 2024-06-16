from flask import render_template
from db.db import DatabaseConnection

def login(username, password):
   if username =="" or password == "":
       empty_err = "you must fill all fields"
       return render_template("login.html", err = empty_err)
   else:
       password = hashlib.md5(password.encode()).hexdigest()
       try:
           with DatabaseConnection() as cur:
               cur.execute("""
               SELECT * FROM users WHERE (username = %s or email = %s) AND password = %s
               """, (username, username, password))
               user = cur.fetchone()
           if user:
               return render_template("user.html", user=user)
           else:
               return render_template("login.html", err="Invalid username or password.")
       except Exception as e:
           print(f"An error occurred: {e}")
           return render_template("login.html", err="An error occurred. Please try again.")