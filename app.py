from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World !"


@app.route("/abault")
def abault():
    return "Sobre!"


# para todo desenvolvimento  local use
if __name__ =="__main__":
    app.run(debug=True)

