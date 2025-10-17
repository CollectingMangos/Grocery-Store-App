from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello how are you"

if __name__ == "__main__":
    print("Starting Python Flask server for Grocery Store App")
    app.run(port=5000)
    