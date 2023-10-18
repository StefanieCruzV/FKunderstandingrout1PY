from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'  

@app.route("/dojo")
def dojo():
    return 'Dojo!'  

@app.route("/<phrase>")
def change_name(phrase):
    return f"Hi {phrase}"

@app.route("/repeat/<int:times>/<phrase>")
def repeat_times(times,phrase,):
    repeated = phrase * times
    return repeated

if __name__ == "__main__":
    app.run(debug=True)