train_path = "data/sigma_cabs.csv"
test_path = "data/test.csv"
model_path = "models/encoded.pickle"
target_column = "Surge_Pricing_Type"

predictor_column = ['Trip_Distance', 'Type_of_Cab', 'Customer_Since_Months',
       'Life_Style_Index', 'Confidence_Life_Style_Index', 'Destination_Type',
       'Customer_Rating', 'Cancellation_Last_1Month', 'Var1', 'Var2', 'Var3',
       'Gender']