import sys
sys.path.append('src')
import joblib
import pickle
import pandas as pd
import datetime
from flask_cors import CORS
from flask import Flask, json, request, jsonify , render_template
from predict import preprocess_and_predict


# This will enable CORS for all routes
'''
Cross-origin resource sharing (CORS) is a browser security feature 
that restricts cross-origin HTTP requests that are initiated from scripts running in the browser.
'''
app = Flask(__name__)
CORS(app) 

# Load data (deserialize)
with open('models/encoded.pickle', 'rb') as handle:
    encoded_dict = pickle.load(handle)
model_path = "models/Logistic Regression.joblib"
model= joblib.load(model_path)


@app.route('/predict', methods=['POST','GET'])
def predict():
    '''
    This function Get the data from the POST request and 
    Convert json data to dataframe and Pre-process and make prediction using model loaded from disk as per the data.
    input:
        params: json data collected from api call.
    returns:
            jsonified prediction value
    '''
    json_data = request.get_json(force=True)
    df = pd.DataFrame.from_dict(pd.json_normalize(json_data), orient='columns')
    data = preprocess_and_predict(df,encoded_dict)
    prediction = model.predict(data)

    # Take the first value of prediction
    result = prediction[0]
    # print("price : ",result)
    return jsonify({'prediction': str(result)})


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)


