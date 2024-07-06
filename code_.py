from flask import Flask 

app = Flask(__name__)

@app.route("/") # the route function tells which URL is associated with the given function.
def hello():
    return "Hello World"

if __name__ == '__main__':
    app.run(debug=True)