# Simka_Birsk_site
# Запустите приложение:
# В терминале перейдите в папку проекта и выполните команду:
# pip install -r requirements.txt
# python app.py

# app.py

from flask import Flask, render_template, request
from config import API_TOKEN

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/price')
def price():
    return render_template('price.html')

@app.route('/working_hours')
def working_hours():
    return render_template('working_hours.html')

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

if __name__ == '__main__':
    app.run(debug=True)

