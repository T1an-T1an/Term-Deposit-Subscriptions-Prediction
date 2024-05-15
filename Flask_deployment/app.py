from flask import Flask, render_template, request, redirect, url_for
import joblib
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

app = Flask(__name__)

# Load the model
model = joblib.load('./stacked_model_five_features.pkl')

# Create the function to create the plots
def create_plots(new_data=None):
    # Load dataset
    df = pd.read_csv('./bank_subset.csv')

    # Randomly sample the data in the specified regions to make the graph more visible
    df_low_duration = df[df['duration'] < 2000].sample(frac=0.02)
    df_low_balance = df[df['balance'] < 20000].sample(frac=0.04)

    # Plotting
    plt.figure(figsize=(10, 5))
    
    # First important feature
    plt.subplot(1, 2, 1)
    sns.stripplot(data=df[df['duration'] >= 2000], x='y', y='duration', jitter=True, size=3, color='blue')
    sns.stripplot(data=df_low_duration, x='y', y='duration', jitter=True, size=3, color='blue')
    plt.xlabel('y')

    # Second important feature
    plt.subplot(1, 2, 2)
    sns.stripplot(data=df[df['balance'] >= 20000], x='y', y='balance', jitter=True, size=3, color='orange')
    sns.stripplot(data=df_low_balance, x='y', y='balance', jitter=True, size=3, color='orange')
    plt.xlabel('y')

    # Add grid and background color (grey)
    plt.subplot(1, 2, 1)
    plt.grid(True, color='white', linestyle='--', linewidth=0.5)
    plt.gca().set_facecolor('lightgray')

    plt.subplot(1, 2, 2)
    plt.grid(True, color='white', linestyle='--', linewidth=0.5)
    plt.gca().set_facecolor('lightgray')

    # If there's new data, plot it with a different marker
    if new_data:
        prediction = model.predict([new_data])
        plt.subplot(1, 2, 1)
        sns.scatterplot(x=[prediction[0]], y=[new_data[0]], label='New Data', marker='X', s=100, color='red', zorder=3)
        plt.subplot(1, 2, 2)
        sns.scatterplot(x=[prediction[0]], y=[new_data[1]], label='New Data', marker='X', s=100, color='red', zorder=3)

    plt.legend()

    plt.tight_layout(pad=3.0)

    # Save the generated plots as an image in the Flask app's directory.
    plot_name = os.path.join('static', 'images', 'plot.png')
    plt.savefig(plot_name)

    return plot_name

# Main
@app.route('/', methods=['GET', 'POST'])
def index():
    # Initializes a message to display on the website and an empty prediction
    message = ""
    prediction = None

    # Check if the request method is POST (if the user has submitted the form).
    if request.method == 'POST':
        # Get user input from the form.
        input_data = request.form['input_data']
        
        # Split the comma-separated string into a list of values.
        values = list(map(float, input_data.split(',')))
        
        # Check if the length of values is as expected (i.e., 5 features).
        if len(values) == 5:
            # Reshape the values to make it suitable for the model's predict method.
            data_for_prediction = np.array(values).reshape(1, -1)
            
            # Use the trained model to predict the class.
            prediction = model.predict(data_for_prediction)[0]
            
            # Update the status message.
            message = f"Predicted Class: {prediction}"
            
            # Create the plots with the user input data.
            create_plots(new_data=values)
        else:
            message = "Please input 5 comma-separated values."
    else:
        # If it's the initial GET request, generate the default plots without user input.
        create_plots()

    # Render the index.html template with the provided values.
    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)