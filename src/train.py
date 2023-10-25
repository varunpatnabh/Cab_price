import os
import sys
import json
import numpy as np
import pandas as pd
import json
import joblib
from sklearn import metrics
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
from sklearn.preprocessing import LabelEncoder
from load_data import load_data
from data_cleaning import data_cleaning
from preprocessing import convert_categorical_columns
from model import model_list


def save_model(model,file_name):
    joblib.dump(model,file_name)


def prepare_training(df,target_column):
    X = df.drop(target_column,axis=1)
    y = df[target_column]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
    return X_train, X_test, y_train, y_test


def model_training(df,target_column,model_list,model_path):
    X_train, X_test, y_train, y_test = prepare_training(df,target_column)
    #le = LabelEncoder()
    #y_train = le.fit_transform(y_train)
    for model_name, model in model_list:
        print("Model Name : ", model_name)
        model = model
        model.fit(X_train,y_train)
        predicted_value = model.predict(X_test)
        train_tested = model.predict(X_train)

        print(predicted_value)
       
        accuracy = accuracy_score(y_test, predicted_value)
        #print("Accuracy:", accuracy)
        print("f1_scores train:",f1_score( y_train,  train_tested, average='micro'))
        #f1_scores = cross_val_score(model, df,target_column, cv=5, scoring='f1_macro')
        print("f1_scores test:",f1_score( y_test,  predicted_value, average='micro'))
        
        save_model(model,os.path.join(model_path, model_name+".joblib"))



if  __name__ == "__main__":

    # reading configuration from config file.
    with open ("config.json",'r') as file:
        config = json.load(file)
    train = config["train_path"]
    model_path = config["model_path"]
    target_column = config["target_column"]

    # Reading Train data
    df = load_data(train)
    df = data_cleaning(df)
    # data cleaning done
    convert_categorical_columns(df,target_column,model_path)
    model_training(df,target_column,model_list,model_path)
    print("model train done")