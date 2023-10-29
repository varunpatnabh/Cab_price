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
    print("price : ",result)
    return jsonify({'prediction': str(result)})


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)



#     @app.route("/prediction", methods=['GET', 'POST'])
# def prediction():
#     # get inputs from webpage
   
#     Trip_ID = request.args.get('Trip_ID'), 
#     Trip_Distance = request.args.get('Trip_Distance') 
#     Type_of_Cab = request.args.get('Type_of_Cab') 
#     Customer_Since_Months = request.args.get('Customer_Since_Months')
#     Life_Style_Index = request.args.get('Life_Style_Index')
#     Confidence_Life_Style_Index = request.args.get('Confidence_Life_Style_Index') 
#     Destination_Type = request.args.get('Destination_Type')
#     Customer_Rating = request.args.get('Customer_Rating')
#     Cancellation_Last_1Month = request.args.get('Cancellation_Last_1Month')
#     Var1 = request.args.get('Var1')
#     Var2 = request.args.get('Var2')
#     Var3 = request.args.get('Var3')
#     Gender = request.args.get('Gender')

#     data_dict = {
#             'Trip_ID' : Trip_ID, 
#             'Trip_Distance' : float(Trip_Distance), 
#             'Type_of_Cab' : Type_of_Cab, 
#             'Customer_Since_Months' : int(Customer_Since_Months),
#             'Life_Style_Index' : float(Life_Style_Index), 
#             'Confidence_Life_Style_Index' : Confidence_Life_Style_Index, 
#             'Destination_Type' : Destination_Type,
#             'Customer_Rating' : float(Customer_Rating), 
#             'Cancellation_Last_1Month' : int(Cancellation_Last_1Month), 
#             'Var1' : int(Var1), 
#             'Var2' : int(Var2), 
#             'Var3' : int(Var3),
#             'Gender' : Gender
#         }
#     print(data_dict)
    
#     # Convert input recieved from webpage as dict to dataframe
#     df = pd.DataFrame.from_dict([data_dict],orient='columns')
#     print(df.dtypes)
#     df.to_csv('test_input.csv',mode='a', header=False, index=False)
#     data = preprocess_and_predict(df,encoded_dict)
#     prediction = model.predict(data)
#     print(str(prediction[0]))
#     return str(prediction[0])