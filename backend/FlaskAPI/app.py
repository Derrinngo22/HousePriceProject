import flask
from flask import Flask, jsonify, request
import json
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

@app.route('/predict', methods=['GET'])
def predict():
    form = request.form
    # load model
    model = get_model()
    oq = float(request.form['OQ'])
    grl = np.log(float(request.form['GRL']))
    gc = float(request.form['GC'])
    tbsf = np.log(float(request.form['TBSF']))
    fb = float(request.form['FB'])
    yb = float(request.form['YB'])
    # oq, grl, gc, tbsf, fb, yb = 5, 123456, 2, 123456, 0, 1979
    input = pd.DataFrame({'OverallQual': oq, 'GrLivArea': grl, 'GarageCars': gc,'TotalBsmtSF': tbsf, 'FullBath': fb , 'YearBuilt': yb}, index=[0])
    prediction = model.predict(input)[0]
    print(str(model.predict(input)[0])+ "asdfasdf")
    response = json.dumps({'response': str(prediction)})
    return response, 200

def get_model():
    return pickle.load(open("models/XGBmodel", 'rb'))


if __name__ == '__main__':
 application.run(debug=True)