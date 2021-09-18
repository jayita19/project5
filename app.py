from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello Jayita!  This is Udacity final project Green Deployment version 2.1"
app.run(host="0.0.0.0", port=8080, debug=True)
