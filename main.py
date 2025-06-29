from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import random
import skops.io as sio
import pandas as pd
import numpy as np

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # penting untuk session
 

@app.route('/')
def hero():
    return render_template('hero.html')

@app.route('/form')
def form():
    torque_list = ['Tidak Terdaftar / Tidak Diketahui', '190Nm@ 2000rpm', '250Nm@ 1500-2500rpm', '12.7@ 2,700(kgm@ rpm)', '22.4 kgm at 1750-2750rpm', '11.5@ 4,500(kgm@ rpm)', '113.75nm@ 4000rpm', '7.8@ 4,500(kgm@ rpm)', '59Nm@ 2500rpm', '170Nm@ 1800-2400rpm', '160Nm@ 2000rpm', '248Nm@ 2250rpm', '78Nm@ 4500rpm', '84Nm@ 3500rpm', '115Nm@ 3500-3600rpm', '200Nm@ 1750rpm', '62Nm@ 3000rpm', '219.7Nm@ 1500-2750rpm', '114Nm@ 3500rpm', '115Nm@ 4000rpm', '69Nm@ 3500rpm', '172.5Nm@ 1750rpm', '6.1kgm@ 3000rpm', '114.7Nm@ 4000rpm', '60Nm@ 3500rpm', '90Nm@ 3500rpm', '151Nm@ 4850rpm', '104Nm@ 4000rpm', '320Nm@ 1700-2700rpm', '250Nm@ 1750-2500rpm', '145Nm@ 4600rpm', '146Nm@ 4800rpm', '343Nm@ 1400-3400rpm', '200Nm@ 1400-3400rpm', '200Nm@ 1250-4000rpm', '138Nm@ 4400rpm', '360Nm@ 1200-3400rpm', '200Nm@ 1200-3600rpm', '380Nm@ 1750-2500rpm', '173Nm@ 4000rpm', '400Nm@ 1750-3000rpm', '400Nm@ 1400-2800rpm', '200Nm@ 1750-3000rpm', '111.7Nm@ 4000rpm', '219.6Nm@ 1500-2750rpm', '112Nm@ 4000rpm', '250Nm@ 1500-3000rpm', '130Nm@ 4000rpm', '205Nm@ 1750-3250rpm', '280Nm@ 1350-4600rpm', '99.04Nm@ 4500rpm', '77Nm@ 3500rpm', '110Nm@ 3750rpm', '153Nm@ 3800rpm', '113.7Nm@ 4000rpm', '114Nm@ 4000rpm', '113Nm@ 4200rpm', '101Nm@ 3000rpm', '290Nm@ 1800-2800rpm', '120Nm@ 4250rpm', '250Nm@ 1500~4500rpm', '96 Nm at 3000 rpm', '360Nm@ 1750-2800rpm', '135Nm@ 2500rpm', '259.8Nm@ 1900-2750rpm', '200Nm@ 1900rpm', '259.9Nm@ 1900-2750rpm', '91Nm@ 4250rpm', '96.1Nm@ 3000rpm', '109Nm@ 4500rpm', '400nm@ 1750-3000rpm', '347Nm@ 4300rpm', '620Nm@ 1600-2400rpm', '400Nm@ 1750-2500rpm', '250@ 1250-5000rpm', '500Nm@ 1600-1800rpm', '550Nm@ 1750-2750rpm', '490Nm@ 1600rpm', '250 Nm at 2750 rpm', '177.5Nm@ 4700rpm', '170Nm@ 1750-4000rpm', '300Nm@ 1200-4000rpm', '300Nm@ 1200-1400rpm', '260Nm@ 1500-2750rpm', '213Nm@ 4500rpm', '224Nm@ 4000rpm', '113Nm@ 4500rpm', '95Nm@ 3000-4300rpm', '13.1kgm@ 4600rpm', '205Nm@ 1800-2800rpm', '190Nm@ 1750-3000rpm', '146Nm at 4800 rpm', '14.9 KGM at 3000 RPM', '115Nm@ 3200rpm', '117nm@ 4000rpm', '320Nm@ 1500-3000rpm', '72Nm@ 4386rpm', '11.4 kgm at 4,000 rpm', '140Nm@ 1500-4000rpm', '134Nm@ 4000rpm', '150Nm@ 4500rpm', '340Nm@ 1800-3250rpm', '240Nm@ 1600-2800rpm', '330Nm@ 1600-2800rpm', '12.5@ 3,500(kgm@ rpm)', '110Nm@ 4800rpm', '111.8Nm@ 4000rpm', '11.8@ 3,200(kgm@ rpm)', '135.4Nm@ 2500rpm', '300Nm@ 1750-2500rpm', '190.25nm@ 1750-2250rpm', '140Nm@ 1800-3000rpm', '20.4@ 1400-3400(kgm@ rpm)', '247Nm@ 1800-2000rpm', '223Nm@ 1600-2200rpm', '180 Nm at 1440-1500rpm', '195Nm@ 1400-2200rpm', '154.9Nm@ 4200rpm', '114.73Nm@ 4000rpm', '160Nm@ 1500-2750rpm', '108Nm@ 4400rpm', '190.24nm@ 1750-2250rpm', '200Nm@ 2000-3500rpm', '420Nm@ 1400-2600rpm', '100Nm@ 2700rpm', '51Nm@ 4000rpm', '250Nm@ 1250-5300rpm', '132Nm@ 3000rpm', '218Nm@ 4200rpm', '85Nm@ 3000rpm', '74.5Nm@ 4000rpm', '160Nm@ 1750rpm', '180.4Nm@ 1750-2500rpm', '230Nm@ 1500-2500rpm', '113.75Nm@ 4000rpm', '219.66nm@ 1500-2750rpm', '245Nm@ 1750rpm', '360Nm@ 1400-3200rpm', '320Nm@ 2000rpm', '135 Nm at 2500  rpm ', '24 KGM at 1900-2750 RPM', '190Nm@ 1750-2250rpm', '204Nm@ 2000-2750rpm', '14.3@ 1,800-3,000(kgm@ rpm)', '125Nm@ 2000rpm', '172Nm@ 4300rpm', '150Nm@ 1750rpm', '102Nm@ 4000rpm', '8.5@ 2,500(kgm@ rpm)', '180Nm@ 1440-1500rpm', '106.5Nm@ 4400rpm', '108.5Nm@ 5000rpm', '350Nm@ 1750-2500rpm', '144.15nm@ 4500rpm', '104Nm@ 4400rpm', '99Nm@ 4500rpm', '200Nm@ 2000rpm', '280Nm@ 1800-2800rpm', '142.5Nm@ 1750rpm', '140Nm@ 4400rpm', '115@ 2,500(kgm@ rpm)', '196Nm@ 5000rpm', '260 Nm at 1800-2200 rpm', '9.8@ 3,000(kgm@ rpm)', '209Nm@ 2000rpm', '24@ 1,900-2,750(kgm@ rpm)', '135 Nm at 2500 rpm', '140Nm@ 4200rpm', '220Nm at 1400-2600 rpm', '48Nm@ 3000rpm', '171Nm@ 1800rpm', '277.5Nm@ 1700-2200rpm', '215Nm@ 3600rpm', '219.6Nm@ 1750-2750rpm', '195Nm@ 1440-2200rpm', '13@ 2,500(kgm@ rpm)', '85Nm@ 2500rpm', '180Nm@ 2000rpm', '200Nm@ 1400-2200rpm', '380Nm(38.7kgm)@ 2500rpm', '110Nm@ 4400rpm', '72Nm@ 4388rpm', '263.7Nm@ 2500rpm', '320Nm@ 1600-2800rpm', '25.5@ 1,500-3,000(kgm@ rpm)', '16.3@ 2,000(kgm@ rpm)', '190 Nm at 1750 rpm ', '94.14Nm@ 3500rpm', '12@ 3,500(kgm@ rpm)', '113Nm@ 5000rpm', '280Nm@ 2400-2800rpm', '13.5@ 2,500(kgm@ rpm)', '96Nm@ 3500rpm', '16@ 2,000(kgm@ rpm)', '320Nm@ 1750-3000rpm', '114.73nm@ 4000rpm', '320Nm@ 1750-2500rpm', '138nm@ 4400rpm', '190Nm@ 1750rpm', '789Nm@ 2250rpm', '259.87Nm@ 1900-2750rpm', '205Nm@ 1750rpm', '436.39Nm@ 1800-2500rpm', '182.5Nm@ 1500-1800rpm', '90.3Nm@ 4200rpm', '12.5@ 2,500(kgm@ rpm)', '14.9@ 3,000(kgm@ rpm)', '215Nm@ 1750-3000rpm', '215Nm@ 1750-3000', '305Nm@ 2000rpm', '540Nm@ 2000rpm', '327Nm@ 2600rpm', '300Nm@ 1600-3000rpm', '620Nm@ 2000-2500rpm', '450Nm@ 1600-2400rpm', '19@ 1,800(kgm@ rpm)', '9.2@ 4,200(kgm@ rpm)', '145@ 4,100(kgm@ rpm)', '51Nm@ 4000+/-500rpm', '110Nm@ 3000rpm', '148Nm@ 3500rpm', '116Nm@ 4750rpm', '48@ 3,000+/-500(NM@ rpm)', '148Nm@ 4000rpm', '222Nm@ 4300rpm', '135.3Nm@ 5000rpm', '98Nm@ 1600-3000rpm', '170Nm@ 1400-4500rpm', '343Nm@ 1400-2800rpm', '402Nm@ 1600-3000rpm', '113Nm@ 3300rpm', '99.07Nm@ 4500rpm', '210nm@ 1600-2200rpm', '190 Nm at 1750  rpm ', '32.1kgm@ 2000rpm', '224nm@ 1500-2750rpm', '400nm@ 1750-2500rpm', '215Nm@ 1750-2500rpm', '25@ 1,800-2,800(kgm@ rpm)', '197Nm@ 1750rpm', '136.3Nm@ 4200rpm', '470Nm@ 1750-2500rpm', '11@ 3,000(kgm@ rpm)', '142Nm@ 4000rpm', '145Nm@ 4100rpm', '320Nm@ 1500-2800rpm', '123Nm@ 1000-2500rpm', '218Nm@ 1400-2600rpm', '510@ 1600-2400', '220Nm@ 1500-2750rpm', '380Nm@ 2000rpm', '104Nm@ 3100rpm', '20@ 3,750(kgm@ rpm)', '46.5@ 1,400-2,800(kgm@ rpm)', '380Nm@ 2500rpm', '15@ 3,800(kgm@ rpm)', '136Nm@ 4250rpm', '228Nm@ 4400rpm', '149Nm@ 4500rpm', '187Nm@ 2500rpm', '146Nm@ 3400rpm', '8.6@ 3,500(kgm@ rpm)', '219.7Nm@ 1750-2750rpm', '300Nm@ 2000rpm', '42@ 2,000(kgm@ rpm)', '110Nm@ 3000-4300rpm', '110(11.2)@ 4800', '330Nm@ 1800rpm', '225Nm@ 1500-2500rpm', '380Nm@ 1750-2750rpm', '28.3@ 1,700-2,200(kgm@ rpm)', '259.88Nm@ 1900-2750rpm', '580Nm@ 1400-3250rpm', '127Nm@ 3500rpm', '300Nm@ 1500-2500rpm', '132.3Nm@ 4000rpm', '113nm@ 4400rpm', '151NM@ 4850rpm', '153Nm@ 3750-3800rpm', '10.7@ 2,500(kgm@ rpm)', '124.6Nm@ 3500rpm', '78Nm@ 3500rpm', '219.9Nm@ 1750-2750rpm', '420.7Nm@ 1800-2500rpm', '130Nm@ 3000rpm', '424Nm@ 2000rpm', '130@ 2500(kgm@ rpm)', '99.8Nm@ 2700rpm', '113Nm@ 4,500rpm', '11.2@ 4,400(kgm@ rpm)', '240Nm@ 1850rpm', '16.1@ 4,200(kgm@ rpm)', '320Nm@ 1750-2700rpm', '115Nm@ 4500rpm', '245Nm@ 4000rpm', '619Nm@ 1600-2400rpm', '380Nm@ 1750-3000rpm', '560Nm@ 1500rpm', '230Nm@ 1500-2250rpm', '90Nm@ 2650rpm', '260Nm@ 1800-2200rpm', '259.87nm@ 1500-3000rpm', '16.6@ 4,500(kgm@ rpm)', '219.66NM@ 1500-2750rpm', '250Nm@ 1500-4500rpm', '14.9@ 3,400(kgm@ rpm)', '25.5@ 1,900(kgm@ rpm)', '33.7@ 1,800(kgm@ rpm)', '285Nm@ 2400-4000rpm', '10.7@ 2,600(kgm@ rpm)', '250Nm@ 1000-2000rpm', '240Nm@ 1750rpm', '226Nm@ 4400rpm', '510Nm@ 1600-2800rpm', '259.87NM@ 1500-3000rpm', '155 Nm at 1600-2800 rpm', '240Nm@ 2000rpm', '103Nm@ 4500rpm', '13.5@ 4,800(kgm@ rpm)', '400Nm@ 1750-2750rpm', '175Nm@ 1500-4100rpm', '135.4Nm@ 2500', '245Nm@ 5000rpm', '57Nm@ 2500rpm', '96Nm@ 2500rpm', '215nm@ 1750-2500rpm', '10.4@ 3,200(kgm@ rpm)', '128Nm@ 3100rpm', '102Nm@ 2600rpm', '131Nm@ 4400rpm', '11.4@ 4,000(kgm@ rpm)', '343Nm@ 1600-2800rpm', '12@ 2500(kgm@ rpm)', '12.4@ 2,600(kgm@ rpm)', '170Nm@ 4200rpm', '176Nm@ 1500rpm', '250Nm@ 1600-2000rpm', '24.5@ 3,500-4,500(kgm@ rpm)', '22.9@ 1,950-4,700(kgm@ rpm)', '113Nm@ 4400rpm', '210 / 1900', '250Nm@ 1250-5000rpm', '400Nm@ 175-2750rpm', '350Nm@ 1500-3500rpm', '175nm@ 1750-4000rpm', '115@ 2500(kgm@ rpm)', '110Nm@ 4500rpm', '190Nm@ 2000-3000rpm', '21.4@ 1,750-4,600(kgm@ rpm)', '96Nm@ 3000rpm', '23.6@ 4,250(kgm@ rpm)', '11.3kgm@ 4700rpm', '450Nm@ 1750-2500rpm', '35.7@ 1,750-3,000(kgm@ rpm)', '6@ 2,500(kgm@ rpm)', '13.9 kgm at 4200 rpm', '320Nm@ 1400-4100rpm', '150Nm@ 1700-4500rpm', '113.8Nm@ 4000rpm', '110@ 3,000(kgm@ rpm)', '62Nm@ 2500rpm', '18@ 1,600-2,200(kgm@ rpm)', '83Nm@ 3000rpm', '124.5Nm@ 3500rpm', '20@ 4,700(kgm@ rpm)', '300Nm@ 1600-4000rpm', '171.6Nm@ 1500-4000rpm', '21.4@ 1,900(kgm@ rpm)', '190@ 21,800(kgm@ rpm)', '5.7@ 2,500(kgm@ rpm)', '88.4Nm@ 4200rpm', '250 Nm at 1,500-3,000 rpm', '340nm@ 1750-3000rpm', '36.6@ 1,750-2,500(kgm@ rpm)', '12.5kgm@ 3500rpm', '6.1@ 3,000(kgm@ rpm)', '110Nm@ 4000rpm', '250Nm@ 4250rpm', '190Nm@ 2000-3000', '175nm@ 1500-4100rpm', '4.8kgm@ 3000rpm', '355Nm@ 4500rpm', '51@ 1,750-3,000(kgm@ rpm)', '119Nm@ 4250rpm', '410Nm@ 1600-2800rpm', '174Nm@ 4300rpm', '99.1Nm@ 4500rpm', '385Nm@ 1600-2500rpm', '180 Nm at 2000rpm', '190 Nm at 1750 rpm', '53@ 2,000-2,750(kgm@ rpm)', '360Nm@ 1400-2600rpm', '124Nm@ 3500rpm', '17.5@ 4,300(kgm@ rpm)', '360Nm@ 2000rpm', '145Nm@ 3750rpm', '85Nm@ 3500rpm', '190 Nm at 2000rpm', '13.5@ 2500(kgm@ rpm)', '250nm@ 1500-3000rpm', '250nm@ 1500-2750rpm', '159.8Nm@ 1500-2750rpm', '500Nm@ 2000rpm', '400nm@ 2800rpm', '33@ 2,000-2,680(kgm@ rpm)', '10.2@ 2,600(kgm@ rpm)', '190Nm@ 4300rpm', '380Nm@ 1750rpm', '250.06nm@ 1500-2750rpm', '90nm@ 3500rpm', '190Nm@ 3700rpm', '436.4Nm@ 1800-2500rpm', '96  Nm at 3000  rpm ']   
    return render_template('form.html', torque_list=torque_list)

@app.route('/predict', methods=['POST'])
def predict():

    brand = request.form.get('brand')
    km_driven = request.form.get('km_driven')
    fuel = request.form.get('fuel')
    seller_type = request.form.get('seller_type')
    transmission = request.form.get('transmission')
    owner = request.form.get('owner')
    mileage = request.form.get('rasioBahanBakar')
    engine = request.form.get('engine')
    max_power = request.form.get('max_power')
    torque = request.form.get('torque')
    seats = request.form.get('seats')
    age = request.form.get('age')


    data_to_predict = pd.DataFrame({
        'brand': [brand],            # String    
        'km_driven': [km_driven],    # Integer
        'fuel': [fuel],              # String
        'seller_type': [seller_type],  # String
        'transmission': [transmission],     # String
        'owner': [owner],                 # String
        'mileage': [mileage],              # Float 
        'engine': [engine],             # Float 
        'max_power': [max_power],           # Float 
        'torque': [torque],                 # Float
        'seats': [seats],                   # Integer
        'age' : [age]                    # Float
    })



    model_filename = 'car_price_prediction_model.skops'

    try:
        loaded_model_pipeline = sio.load(model_filename, trusted=['sklearn.compose._column_transformer._RemainderColsList', 'xgboost.core.Booster', 'xgboost.sklearn.XGBRegressor'])
        print(f"Model '{model_filename}' loaded successfully!")
    except FileNotFoundError:
        print(f"Error: The file '{model_filename}' was not found.")
        print("Please ensure the .skops file is in the same directory as this script, or provide its full path.")
        exit()

    y_pred_log = loaded_model_pipeline.predict(data_to_predict)
    predicted_price = np.expm1(y_pred_log)

    rupees_to_rupiah_rate = 189.91



    # Simpan hasil ke session untuk ditampilkan di /result
    session['predicted_price'] = float(predicted_price[0]) * rupees_to_rupiah_rate
    session['mae'] = 20000
    return redirect(url_for('result'))

@app.route('/result')
def result():
    price = session.get('predicted_price', None)
    mae = session.get('mae', None)
    return render_template('result.html', price=price, mae=mae)



    



if __name__ == '__main__':
    app.run(debug=True)
