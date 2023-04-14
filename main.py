from flask import Flask
from flask import render_template, request, redirect

app = Flask(__name__)

@app.route('/warehouse/', methods=['GET', 'POST'])

@app.route("/warehouse")
def warehouse():
    items = ["screwdriver", "hammer", "saw"]
    errors = ["hammer is broken!"]
    return render_template("warehouse.html", items=items, errors=errors)

if __name__ == "__main__": 
    app.run()

