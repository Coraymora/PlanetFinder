from flask import Flask, render_template, url_for, request, redirect
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=('GET', 'POST'))
def index():
    return render_template('index.html')

@app.route('/result/', methods=['POST'])
def result():
    location = request.form.get("location")
    planet = request.form.get("planet")
    
    return render_template('result.html')

if __name__ == "__main__":
    app.run(debug=True)
