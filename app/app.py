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
model_path = "models/Random Forest.joblib"
model= joblib.load(model_path)




@app.route('/api', methods=['POST','GET'])
def predict():
    # Get the data from the POST request.
    json_data = request.get_json(force=True)

    # Convert json data to dataframe
    df = pd.DataFrame.from_dict(pd.json_normalize(json_data), orient='columns')
    print("-"*80)
    print(df)

    # Pre-process and make prediction using model loaded from disk as per the data.
    data = preprocess_and_predict(df,encoded_dict)
    print("-"*80)
    print(data)
    print("-"*80)

    prediction = model.predict(data)


    # Take the first value of prediction
    output = prediction[0]
    print("price : ",output)
    return jsonify(str(output))


@app.route("/prediction", methods=['GET', 'POST'])
def prediction():
    # get inputs from webpage
   
    Trip_ID = request.args.get('Trip_ID'), 
    Trip_Distance = request.args.get('Trip_Distance') 
    Type_of_Cab = request.args.get('Type_of_Cab') 
    Customer_Since_Months = request.args.get('Customer_Since_Months')
    Life_Style_Index = request.args.get('Life_Style_Index')
    Confidence_Life_Style_Index = request.args.get('Confidence_Life_Style_Index') 
    Destination_Type = request.args.get('Destination_Type')
    Customer_Rating = request.args.get('Customer_Rating')
    Cancellation_Last_1Month = request.args.get('Cancellation_Last_1Month')
    Var1 = request.args.get('Var1')
    Var2 = request.args.get('Var2')
    Var3 = request.args.get('Var3')
    Gender = request.args.get('Gender')

    data_dict = {
            'Trip_ID' : Trip_ID, 
            'Trip_Distance' : Trip_Distance, 
            'Type_of_Cab' : Type_of_Cab, 
            'Customer_Since_Months' : Customer_Since_Months,
            'Life_Style_Index' : Life_Style_Index, 
            'Confidence_Life_Style_Index' : Confidence_Life_Style_Index, 
            'Destination_Type' : Destination_Type,
            'Customer_Rating' :Customer_Rating, 
            'Cancellation_Last_1Month' :Cancellation_Last_1Month, 
            'Var1' : Var1, 
            'Var2' : Var2, 
            'Var3' : Var3,
            'Gender' : Gender
        }
    print(data_dict)
    
    # Convert input recieved from webpage as dict to dataframe
    df = pd.DataFrame.from_dict([data_dict],orient='columns')

    df.to_csv('test_input.csv',mode='a', header=False, index=False)
    data = preprocess_and_predict(df,encoded_dict)
    prediction = model.predict(data)
    return str(prediction[0])


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)