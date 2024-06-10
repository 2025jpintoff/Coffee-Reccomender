from flask import Flask, render_template, request
from model import recommend

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/results", methods=["POST"])
def results():
    fname = request.form["fname"]
    lname = request.form["lname"]
    temperature = request.form["temperature"]
    size = request.form["size"]
    strength = request.form["strength"]
    sweet = request.form["sweet"]
    flavor = request.form["flavor"]
    milk = request.form["milk"]
    
    results = recommend(temperature, size, strength, sweet, flavor, milk)
    return render_template("results.html", fname=fname, lname=lname, results=results)

if __name__ == '__main__':
    app.run(debug=True)

