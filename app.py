from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

data_inicio = datetime(2017, 10, 10, 0, 0, 0)

@app.route("/")
def home():
    return render_template("index.html", data_inicio=data_inicio.strftime("%Y-%m-%dT%H:%M:%S"))

if __name__ == "__main__":
    app.run(debug=True)
