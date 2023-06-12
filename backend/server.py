from flask import Flask , request , jsonify

app = Flask(__name__)

@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == "__main__":
    print("start python Flask server for Grocery store management system")
    app.run(port=5000)