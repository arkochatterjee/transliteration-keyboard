from flask import Flask, render_template, request, send_file, flash, redirect, session, abort, url_for, jsonify
import pymysql
import json
from flask_wtf.csrf import CsrfProtect
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


if __name__ == "__main__":
	app.run(host='0.0.0.0', port=8001, debug=True)