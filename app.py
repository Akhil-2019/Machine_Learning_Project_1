from flask import Flask

app = Flask(__name__)

@app.route("/",methods=['Get','POST]'])
def index():
    return "ML PROJECT"


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8001, debug=True)