from flask import Flask

app = Flask(__name__)

@app.route('/')
   return "hiii"
@app.route("/python")
def home():
    return "Hello from Python App 🚀"

@app.route('/health')
def health():
    return "OK", 200

app.run(host="0.0.0.0", port=5000)
