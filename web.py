from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('pagina2.html')

@app.route("/meses")
def meses():
    return render_template("meses.html")


if __name__ == "__main__":
    app.run(debug=True)
