from flask import Flask, render_template, request, redirect, url_for, session
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # penting untuk session


@app.route('/')
def hero():
    return render_template('hero.html')

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/predict', methods=['POST'])
def predict():
    
    year = request.form.get('year')
    km_driven = request.form.get('km_driven')
    fuel = request.form.get('fuel')
    seller_type = request.form.get('seller_type')
    transmission = request.form.get('transmission')
    owner = request.form.get('owner')

   
    predicted_price = random.randint(200000, 2000000)

    session['predicted_price'] = predicted_price
    return redirect(url_for('result'))

@app.route('/result')
def result():
    price = session.get('predicted_price', None)
    return render_template('result.html', price=price)

if __name__ == '__main__':
    app.run(debug=True)
