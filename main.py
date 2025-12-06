from flask import Flask, render_template, request
import pandas as pd
import pickle

app = Flask(__name__)

# Load cleaned data and model
data = pd.read_csv("Cleaned_data.csv")
pipe = pickle.load(open("RidgeModel.pkl", "rb"))


@app.route('/')
def index():
    locations = sorted(data['location'].unique())
    return render_template('index.html', locations=locations)


@app.route('/predict', methods=['POST'])
def predict():
    # Get values from form
    location = request.form.get('location')
    sqft = request.form.get('total_sqft')  # Changed from 'sqft' to 'total_sqft'
    bath = request.form.get('bath')
    bhk = request.form.get('bhk')

    # Prepare input dataframe
    input_df = pd.DataFrame([[location, sqft, bath, bhk]],
                            columns=['location', 'total_sqft', 'bath', 'bhk'])

    # Predict price
    prediction = pipe.predict(input_df)[0]

    # Return to template with prediction
    locations = sorted(data['location'].unique())
    return render_template('index.html',
                           locations=locations,
                           prediction=str(round(prediction, 2)) + " Lakhs")


if __name__ == "__main__":
    app.run(debug=True, port=5081)


