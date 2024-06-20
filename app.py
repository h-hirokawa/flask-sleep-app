import time
from flask import Flask

app = Flask(__name__)

@app.route('/<seconds>')
def home(seconds=0):
    time.sleep(int(seconds))
    name = "Hello World"
    return name

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
