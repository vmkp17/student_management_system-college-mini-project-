from flask import Flask, render_template, request
from database import connection, cursor

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/add", methods=["GET", "POST"])
def add():

    if request.method == "POST":

        name = request.form["name"]
        roll = request.form["roll"]
        department = request.form["department"]
        marks = int(request.form["marks"])

        if marks >= 90:
            grade = "A+"
        elif marks >= 80:
            grade = "A"
        elif marks >= 70:
            grade = "B"
        elif marks >= 60:
            grade = "C"
        elif marks >= 50:
            grade = "D"
        else:
            grade = "F"

        sql = """
        INSERT INTO students
        (name, roll_no, department, marks, grade)
        VALUES (%s,%s,%s,%s,%s)
        """

        values = (name, roll, department, marks, grade)

        cursor.execute(sql, values)

        connection.commit()

        return "Student Added Successfully"

    return render_template("add.html")


@app.route("/display")
def display():

    cursor.execute("SELECT * FROM students")

    students = cursor.fetchall()

    return render_template("display.html", students=students)

@app.route("/search", methods=["GET","POST"])
def search():

    student = None

    if request.method == "POST":

        roll = request.form["roll"]

        cursor.execute("SELECT * FROM students WHERE roll_no=%s",(roll,))

        student = cursor.fetchone()

    return render_template("search.html", student=student)



@app.route("/delete", methods=["GET","POST"])
def delete():

    if request.method == "POST":

        roll = request.form["roll"]

        cursor.execute("DELETE FROM students WHERE roll_no=%s",(roll,))

        connection.commit()

        return "Student Deleted Successfully"

    return render_template("delete.html")






@app.route("/update", methods=["GET","POST"])
def update():

    if request.method == "POST":

        roll = request.form["roll"]

        marks = int(request.form["marks"])

        if marks >= 90:
            grade="A+"
        elif marks >= 80:
            grade="A"
        elif marks >= 70:
            grade="B"
        elif marks >= 60:
            grade="C"
        elif marks >= 50:
            grade="D"
        else:
            grade="F"

        cursor.execute(
            "UPDATE students SET marks=%s, grade=%s WHERE roll_no=%s",
            (marks, grade, roll)
        )

        connection.commit()

        return "Student Updated Successfully"

    return render_template("update.html")

if __name__ == "__main__":
    app.run(debug=True)