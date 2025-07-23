from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Thanks for following the tutorial!'
