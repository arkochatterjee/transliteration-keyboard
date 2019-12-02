from flask import Flask, render_template, request, send_file, flash, redirect, session, abort, url_for, jsonify
import json
import requests

app = Flask(__name__)



@app.route('/', methods=['GET'])
def index():
    lang = [ 'hindi', 'tamil', 'telugu', 'bengali', 'gujarati', 'marathi', 'kannada', 'malayalam', 'punjabi', 'nepali']
    if session['lang']:
        return render_template('index2.html', lang = lang, langSession =session['lang'])
    else:
        return render_template('index2.html', lang = lang)

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    clicked = None
    if request.method == "POST":
        clicked=request.form['data']
        language=request.form['lang']
        print(clicked)
        print(language)
        session['lang'] = language

        #Calling API to search for transliteration
        api = "http://xlit.quillpad.in/quillpad_backend2/processWordJSON?lang={0}&inString={1}".format(language,clicked)
        response = requests.get(str(api))
        output = (response.json())

        print(output)
        options = (output['twords'][0]['options'])
        itrans = output['itrans']

        if itrans not in options:
            options.append(itrans)
        

        return json.dumps(options)

app.secret_key = "transliteration-keyboard"

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=8001, debug=True)