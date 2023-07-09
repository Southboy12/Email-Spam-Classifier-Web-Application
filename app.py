# Import the Flask class from the flask module
from flask import Flask, render_template, request
import pickle

# Create an instance of the Flass class
app = Flask(__name__)

# Load the trained models
cv = pickle.load(open("models/cv.pkl", 'rb'))  # Load the CountVectorizer model
clf = pickle.load(open("models/clf.pkl", 'rb'))  # Load the classifier model

# Register a route for the home page
@app.route('/')
def home():
    return render_template('index.html')   # Render the HTML template for the home page

# Register a route for the prediction endpoint
@app.route("/predict", methods=["POST"])
def predict():
    email = request.form.get('content')   # Get the emil content from the form submitted in the HTML template
    tokenized_email = cv.transform([email])   # Transform the email text using the CountVectorizer model
    prediction = clf.predict(tokenized_email)   # Make a prediction using the classifier model
    prediction = 1 if prediction == 1 else -1   # Adjust the prediction value if needed
    return render_template("index.html", prediction=prediction, email=email)   # Render the HTML template with the prediction and email data

# Run the flask application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)