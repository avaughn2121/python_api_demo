from flask import Flask, url_for
app = Flask(__name__)

@app_route('/')
def api_root():
    return 'Welcome'

