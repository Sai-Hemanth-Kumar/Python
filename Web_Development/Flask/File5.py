from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home() :
    return render_template("home.html")

@app.route("/contact", methods=["GET", "POST"])
def contact() :
    if request.method == "POST" :
        name = request.form["name"]
        age = request.form["age"]
        gender = request.form["gender"]
        email = request.form["email"]
        return "Thank you for your submission, {}!".format(name)
    return render_template("home5.html")
if __name__ == "__main__" :
    app.run(debug = True)