from flask import Flask, render_template, request
from db import adddb, loaddb, lendb, deldb
app = Flask(__name__)
lenth = lendb()

# Route for the add page
@app.route("/", methods=["GET", "POST"])
def add():
    if request.method == "POST" and 'view' in request.form:
        return render_template('data.html')
    elif request.method == "POST" and 'add' in request.form:
        note = request.form['Text1']
        adddb(note)
        return render_template('add.html')

    return render_template('add.html')

# Route for viewing and editing entries
@app.route("/view", methods=["GET", "POST"])
def view():
    oldnotes = loaddb()

    if request.method == "POST" and "addnew" in request.form:
        return render_template('add.html')
    elif request.method == "POST" and "delete_note" in request.form:
        note = request.form.get("delete_note")
        deldb(note)
        oldnotes = loaddb()

    return render_template('data.html', content=oldnotes)

if __name__ == "__main__":
    app.run(debug=True)