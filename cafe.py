from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/order')
def order():
    return render_template('order.html')

app.run(debug=True)