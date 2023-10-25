import os
import sys
import pandas as pd

def fill_values(df):
    '''
        this function will fill all the missing value
        params : data frame
        return : dataframe without null values
    '''
    # filling the null values in "type_of_Cab" with a new variable
    df["Type_of_Cab"] = df["Type_of_Cab"].fillna("F")

    # filling "Customer_Since_Months" column with the mean of the same column
    df['Customer_Since_Months'].fillna(int(df['Customer_Since_Months'].mean()),inplace = True)

    #filling 'Var1' column with the mean value of that column
    df['Var1'].fillna(int(df['Var1'].mean()),inplace = True)

    #As the no. of lifestyle index and confidence life style index has same nan value so assuming it as one different entity
    df['Life_Style_Index'].fillna(int(df['Life_Style_Index'].mean()),inplace = True)
    
    df['Confidence_Life_Style_Index'] = df['Confidence_Life_Style_Index'].fillna("D")

    return df



def drop_col(df):
    '''
        this function to drop unwanted column which are not useful.
        param : Dataframe
        return : dataframe with all meaningfull column
    '''
    cols_to_drop = ['Trip_ID',]
    df = df.drop(cols_to_drop,axis = 1)
    return df


def type_conversion(df):
    '''
    This function is to convert columns into appropiate datatype.
    params:
        df : Dataframe to be processed
    return: 
        Processed Dataframe

    Trip_ID                         object
    Trip_Distance                  float64
    Type_of_Cab                     object
    Customer_Since_Months          float64
    Life_Style_Index               float64
    Confidence_Life_Style_Index     object
    Destination_Type                object
    Customer_Rating                float64
    Cancellation_Last_1Month         int64
    Var1                           float64
    Var2                             int64
    Var3                             int64
    Gender                          object
    Surge_Pricing_Type               int64
    '''
    df = df.astype(
                    {'Customer_Since_Months': 'int', 
                    
                    'Trip_Distance':'float64',
                    
                    'Var1':'int',
                    'Var2':'int',
                    'Var3':'int'
                    }

                )
    return df


def handle_missing_value(df):
    '''
    This function is to handles missing values in  data.
    '''
    df.dropna(inplace = True)
    return df


def data_cleaning(df):
    '''
    this function will be main function to deal with all data cleaning, 
    it will contain multiple function
    params:
            it will directly take the loaded dataframe
    return : Will give cleaned datafram  for further use
    '''
    df = fill_values(df)
    df = drop_col(df)
    df = type_conversion(df)
    df = handle_missing_value(df)
    
    return df