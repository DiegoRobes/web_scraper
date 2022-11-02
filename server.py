import os
import csv
from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.secret_key = os.environ.get('SERVER_KEY')
Bootstrap(app)

with open('Hugo Award Winners.csv', newline='') as file:
    data = csv.reader(file, delimiter=',')
    rows = []
    for i in data:
        rows.append(i)


@app.route("/")
def home():
    return render_template("index.html", years=rows)


if __name__ == '__main__':
    app.run(debug=True)
