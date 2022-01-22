from flask import Flask, render_template
import os
import sys
# import pyodbc

app = Flask(__name__)

database_url = os.environ("DB_URL")
connection = pyodbc.connect(
        "Driver={SQL Server};"
        f"Server={database_url};"
        "Database=momandpopsdatabase;"
        "Trusted_Connection=yes;"
        )


def get_employees():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM employees")

    employee_row = []
    for employee_info in cursor:
        # gives tuples in the form (firstname, lastname, email address, id)
        data = (f"{employee_info[1]}, {employee_info[0]}", f"{employee_info[2]}")
        employee_row.append(data)

    return employee_row

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/products")
def products():
    return render_template("products.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

# supposed to be hidden to everyone who is unaware of this page... this is not very effective but oh well
@app.route("/momandpops-employees")
def employees():
    return render_template("employees.html", data=get_employees())

if __name__ == '__main__':
	app.run(debug=(len(sys.argv)>1 and sys.argv[1]=="--debug"))
