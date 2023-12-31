import os
import sys
import json
import pandas as pd
import numpy as np
from datetime import datetime


def load_data(train_path):
    '''
        This function is to load data in csv format
        params: input path of the csv 
            
        return : dataframe
    '''
    df = pd.read_csv(train_path)
    return df
