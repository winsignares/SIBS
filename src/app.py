#10.230.16.229
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hola Mundo!! Dulfran xD"

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')