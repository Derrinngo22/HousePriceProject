from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd
from .app import app

@app.route('/')
def show_predict_house_form():
    return render_template('predictorform.html') # look in templates folder


@app.route('/results', methods=['POST'])
def results():
    form = request.form
    if request.method == 'POST':
        #write your function that loads the model
        model = get_model() #you can use pickle to load the trained model
        oq = float(request.form['OQ'])
        grl = np.log(float(request.form['GRL']))
        gc = float(request.form['GC'])
        tbsf = np.log(float(request.form['TBSF']))
        fb = float(request.form['FB'])
        yb = float(request.form['YB'])
        input = pd.DataFrame({'OverallQual': oq, 'GrLivArea': grl, 'GarageCars': gc,'TotalBsmtSF': tbsf, 'FullBath': fb , 'YearBuilt': yb}, index=[0])
        predicted_house_price = model.predict(input)
        
        return render_template('resultform.html', gc=gc,   predicted_price=np.expm1(predicted_house_price))

def get_model():
    return pickle.load(open("other_files/model", 'rb'))