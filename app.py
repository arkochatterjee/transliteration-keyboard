from flask import Flask, render_template, request, send_file, flash, redirect, session, abort, url_for, jsonify
import pymysql
import json
from flask_wtf.csrf import CsrfProtect
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    clicked = None
    if request.method == "POST":
        clicked=request.form['data']
        language=request.form['lang']
        print(clicked)
        print(language)

        #Calling API to search for transliteration
        api = "http://xlit.quillpad.in/quillpad_backend2/processWordJSON?lang={0}&inString={1}".format(language,clicked)
        response = requests.get(str(api), verify=False)
        output = (response.json())

        print(output)
        options = (output['twords'][0]['options'])
        

        return json.dumps(options)


if __name__ == "__main__":
	app.run(host='0.0.0.0', port=8001, debug=True)