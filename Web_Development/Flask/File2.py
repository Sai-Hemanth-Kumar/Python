from flask import Flask

app = Flask(__name__)

@app.route("/")
def home() :
    return "This is Home Page"

@app.route("/about")
def about() :
    return "This is About Page"

@app.route("/contact")
def contact() :
    return "This is Contact Page"

if __name__ == "__main__" :
    app.run(debug = True)