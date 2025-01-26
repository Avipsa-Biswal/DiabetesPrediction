from django.shortcuts import render
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def contactus(request):
    return render(request, 'contactus.html')

def predict(request):
    return render(request, 'predict.html')

def result(request):
    try:
        # Try reading the CSV file
        data = pd.read_csv("C:/Users/USER/DiabetesProject/diabetes.csv")

        # Prepare the data
        X = data.drop("Outcome", axis=1)
        Y = data['Outcome']

        # Split the data into training and testing sets
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

        # Train the logistic regression model
        model = LogisticRegression(max_iter=1000)
        model.fit(X_train, Y_train)

        # Retrieve and process user input
        val1 = float(request.GET['n1'])
        val2 = float(request.GET['n2'])
        val3 = float(request.GET['n3'])
        val4 = float(request.GET['n4'])
        val5 = float(request.GET['n5'])
        val6 = float(request.GET['n6'])
        val7 = float(request.GET['n7'])
        val8 = float(request.GET['n8'])

        # Make the prediction
        pred = model.predict([[val1, val2, val3, val4, val5, val6, val7, val8]])

        # Prepare the result based on prediction
        if pred == [1]:
            result1 = "Positive"
        else:
            result1 = "Negative"

        return render(request, 'predict.html', {"result2": result1})

    except FileNotFoundError:
        # Handle error if CSV file is not found
        error_message = "The dataset file was not found. Please check the file path."
        return render(request, 'predict.html', {"error": error_message})

    except ValueError as e:
        # Handle invalid input data
        error_message = f"Invalid input value: {e}. Please ensure all fields are filled with valid numeric values."
        return render(request, 'predict.html', {"error": error_message})

    except KeyError as e:
        # Handle missing input data (e.g., a field is not in the request)
        error_message = f"Missing input data: {e}. Please provide all required values."
        return render(request, 'predict.html', {"error": error_message})

    except Exception as e:
        # General error handling for any other issues
        error_message = f"An error occurred: {e}. Please try again later."
        return render(request, 'predict.html', {"error": error_message})
