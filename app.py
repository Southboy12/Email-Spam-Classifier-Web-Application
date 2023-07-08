# Import the Flask class from the flask module
from flask import Flask, render_template, request
import pickle

# Create an instance of the Flass class
app = Flask(__name__)
cv = pickle.load(open("models/cv.pkl", 'rb'))
clf = pickle.load(open("models/clf.pkl", 'rb'))

# Register a route
@app.route('/')
def home():
    return render_template('index.html')

@app.route("/predict", methods=["POST"])
def predict():
    email = request.form.get('content')
    tokenized_email = cv.transform([email])
    prediction = clf.predict(tokenized_email)
    prediction = 1 if prediction == 1 else -1
    return render_template("index.html", prediction=prediction, email=email)

# Run the flask application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)