from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route("/")
def main () :
    return render_template('birthday.html')

if __name__== "__main__":
    app.run(debug=True)