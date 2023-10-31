function predictSurgePricing() {
    event.preventDefault(); // Prevent the default form submission behavior

    // Retrieve and collecting all the input values
    const Trip_ID = document.getElementById('Trip_ID').value;
    const Trip_Distance = parseFloat(document.getElementById('Trip_Distance').value);
    const Type_of_Cab = document.getElementById('Type_of_Cab').value;
    const Customer_Since_Months = parseFloat(document.getElementById('Customer_Since_Months').value);
    const Life_Style_Index = parseFloat(document.getElementById('Life_Style_Index').value);
    const Confidence_Life_Style_Index = document.getElementById('Confidence_Life_Style_Index').value;
    const Destination_Type = document.getElementById('Destination_Type').value;
    const Customer_Rating = parseFloat(document.getElementById('Customer_Rating').value);
    const Cancellation_Last_1Month = parseInt(document.getElementById('Cancellation_Last_1Month').value);
    const Var1 = parseFloat(document.getElementById('Var1').value);
    const Var2 = parseInt(document.getElementById('Var2').value);
    const Var3 = parseInt(document.getElementById('Var3').value);
    const Gender = document.getElementById('Gender').value;

    var inputData = {'Trip_ID' : Trip_ID, 
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


    // console.log("Passed data for prediction are : ",inputData);

    // Check if any field is empty
    if (Trip_ID === '' || isNaN(Trip_Distance) || Type_of_Cab === '' || isNaN(Customer_Since_Months) || isNaN(Life_Style_Index) || Confidence_Life_Style_Index === '') {
        alert('Please fill out all fields before submitting.');
        return;
    }

    // Send a POST request to your Flask API
    fetch('http://localhost:5000/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(inputData)
    })
    .then(response => response.json())
    .then(data => handlePrediction(data.prediction));
}


function handlePrediction(prediction) {
    // Update the UI with the predicted value
    document.getElementById('predictedValue').textContent = 'Predicted Surge Pricing Type: ' + prediction;
    document.getElementById('predictionResult').classList.remove('hidden');
}


function resetForm() {
    document.getElementById('predictionForm').reset();
    document.getElementById('predictionResult').classList.add('hidden');
}
