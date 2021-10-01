from flask import Flask

app = Flask(__name__)

@app.route("/")
def display():
    return 'root'

@app.route("/affluence")
def display_affluence():
    return 'affluence'

@app.route("/lieu")
def display_lieu():
    return 'lieu'

if __name__ == "__main__":
    app.run()