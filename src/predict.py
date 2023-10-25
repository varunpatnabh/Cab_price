import json
import pickle
import joblib
import pandas as pd
from load_data import load_data 
from data_cleaning import data_cleaning
from configuration import predictor_column

def decode_predict_input(df,encoded_dict):
    '''
    This function decodes categorical values with same values as done training encoded values.
    Input:
        df : DataFrame
        encoded_dict : Category encoded dictionary
    returns :None
    '''
    #Processing Ordinal Columns  
    Gender_dict = encoded_dict['ordinal_dict']['Gender_dict']
    df['Gender'] = df['Gender'].apply(lambda x: Gender_dict[x])
    Confidence_Life_Style_Index_dict = encoded_dict['ordinal_dict']['Confidence_Life_Style_Index_dict']
    df['Confidence_Life_Style_Index'] = df['Confidence_Life_Style_Index'].apply(lambda x: Confidence_Life_Style_Index_dict[x])
    

    #Processing Nominal Columns
    Type_of_Cab_dict = encoded_dict['nominal_dict']['Type_of_Cab_dict']
    df['Type_of_Cab'] = df['Type_of_Cab'].apply(lambda x: Type_of_Cab_dict[x])
    Destination_Type_dict = encoded_dict['nominal_dict']['Destination_Type_dict']
    df['Destination_Type'] = df['Destination_Type'].apply(lambda x: Destination_Type_dict[x])
    
    


    print(df)
  
def preprocess_and_predict(df,encoded_dict):

    
    '''
      This function takes in new dataframe or row of observation and generate all features
    Input :
        df : DataFrame or row of observation
        encoded_dict : Dictonary created while training for Categorical Encoded Value.
    '''
    data_cleaning(df)
    print(" preprocess and predict:",df.info)
    decode_predict_input(df,encoded_dict)
    X = df[predictor_column]
    return X

if __name__ == "__main__":
    with open(r"models/encoded.pickle", "rb") as input_file:
        encoded_dict = pickle.load(input_file)
    df = pd.read_csv("data/test.csv")
    saved_model= joblib.load("models/Random Forest.joblib")
    data = preprocess_and_predict(df,encoded_dict)
   
    print(saved_model.predict(data.iloc[0:5,:]))