import os
import sys
import pandas as pd


'''
def 
    type_of_vehicle_dict = df.groupby(['Type_of_vehicle'])[target_column].mean().to_dict()
'''
def encoding(df,col,target_col):
    dicts = df.groupby([col])[target_col].mean().to_dict()
    df[col] = df[col].apply(lambda x: dicts[x])
    return dicts


def convert_categorical_to_numerical(df,target_col):
    '''
        this function will be converting categorical to numerical
        param : Dataframe
        return :dataframe with all numerical values
    '''
    cat_col = ['Type_of_Cab','Confidence_Life_Style_Index','Gender']
    encoding_cat_dict ={}
    for col in cat_col:
        encoding_cat_dict[col+'_dict'] = encoding(df,col,target_col)





    

