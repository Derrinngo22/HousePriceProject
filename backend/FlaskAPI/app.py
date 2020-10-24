#https://medium.com/fintechexplained/flask-host-your-python-machine-learning-model-on-web-b598151886d
import flask
from flask import Flask, jsonify, request, render_template
import json
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)
def get_model():
    return pickle.load(open("models/XGBmodel", 'rb'))
model = get_model()

@app.route('/')
def show_predict_house_form():
    return render_template('home.html') 

@app.route('/results', methods=['POST'])
def predict():
    form = request.form
    # load model
    
    oq = float(form['OQ'])
    grl = np.log(float(request.form['GRL']))
    gc = float(request.form['GC'])
    tbsf = np.log(float(request.form['TBSF']))
    fb = float(request.form['FB'])
    yb = float(request.form['YB'])
    # oq, grl, gc, tbsf, fb, yb = 5, 123456, 2, 123456, 0, 1979
    input = pd.DataFrame({'OverallQual': oq, 'GrLivArea': grl, 'GarageCars': gc,'TotalBsmtSF': tbsf, 'FullBath': fb , 'YearBuilt': yb}, index=[0])
    prediction = model.predict(input)
    # response = json.dumps({'response': str(prediction)})
    return render_template('result.html', gc=gc,   predicted_price=np.expm1(prediction))
    




if __name__ == '__main__':
 app.run(debug=True)