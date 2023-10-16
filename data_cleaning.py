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
    df['Customer_Since_Months'].fillna(int(df['Customer_Since_Months'].mean()))

    #filling 'Var1' column with the mean value of that column
    df['Var1'].fillna(int(df['Var1'].mean()))
    return df


def drop_col(df):
    '''
        this function to drop unwanted column which are not useful.
        param : Dataframe
        return : dataframe with all meaningfull column
    '''
    df = df.drop('Trip_ID',axis = 1,inplace = True)
    return df



def data_cleaning(df):
    '''
    this function will be main function to deal with all data cleaning, 
    it will contain multiple function
    params:
            it will directly take the loaded dataframe
    return : Will give cleaned datafram  for further use
    '''
    df = drop_col(df)
    df = fill_values(df)
    return df