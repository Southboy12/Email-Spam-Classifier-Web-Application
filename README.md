# Email Spam Classifier

This is a simple web application that demonstrates an email spam classifier. It uses Flask, a Python web framework, to handle the server-side logic, and HTML templates for the user interface. 

## Table of Contents

- [Features](#feature-1)
- [Installation](#installation)
- [Usage](#Usage)
- [Contributing](#contributing)
- [License](lLicense)
- [Contact](#contact)

## Features

- Email Spam Classification: The application allows users to enter an email and classifies it as either spam or not spam using a pre-trained classifier model.
- User-friendly Interface: The interface provides a text area for users to type or paste their email content, and buttons to submit the email for classification or reset the form.
- Dynamic Results: The classification result is displayed dynamically on the page based on the prediction made by the classifier model.

## Installation

To run this application locally, follow these steps:

1. Clone the repository:

```python
git clone https://github.com/your-username/email-spam-classifier.git
```

2. Install the required dependencies. It is recommended to use a virtual environment:

```python
cd email-spam-classifier
python -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate  # For Windows
pip install -r requirements.txt
```

3. Download the trained models (cv.pkl and clf.pkl) and place them in the "models" directory.