from flask import Flask

app = Flask(__name__)

@app.route('/')
def root():
    return "hiii"

@app.route('/python')
def python_app():
    return "Hello from Python App 🚀"

@app.route('/health')
def health():
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
