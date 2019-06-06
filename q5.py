from flask import Flask, render_template

app = Flask(__name__)



@app.route("/")
def myname():
    return 'Anjana Joy \n 6143'


@app.route("/q5page")
def q5page():
    return render_template("q5page.html")


if __name__ == '__main__':
    app.run()
