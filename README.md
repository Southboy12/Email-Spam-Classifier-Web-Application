# Email Spam Classifier

![Homepge](/Screenshots/Homepage.png)

This is a simple web application that demonstrates an email spam classifier. It uses Flask, a Python web framework, to handle the server-side logic, and HTML templates for the user interface. 

## Table of Contents

- [Features](#feature)
- [Installation](#installation)
- [Usage](#usage)
- [Customization](#customization)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#lLicense)

## Features

- Email Spam Classification: The application allows users to enter an email and classifies it as either spam or not spam using a pre-trained classifier model.
- User-friendly Interface: The interface provides a text area for users to type or paste their email content, and buttons to submit the email for classification or reset the form.
- Dynamic Results: The classification result is displayed dynamically on the page based on the prediction made by the classifier model.

## Installation

If you want to run this application locally, here's what you need to do.:

1. Clone the repository:

```python
git clone https://github.com/your-username/email-spam-classifier.git
```

2. Install the required dependencies. I recommend using a virtual environment for your Python projects:

```python
cd email-spam-classifier
python -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate  # For Windows
pip install -r requirements.txt
```

3. Download the trained models (cv.pkl and clf.pkl) and place them in the "models" directory.

## Usage

1. Start the Flask server:

```python
python app.py
```

2. Open your web browser and go to http://localhost:8080 to access the application.

3. Upon accessing the application, you will see the title "EMAIL SPAM CLASSIFIER" displayed.

4. The main section of the page contains a form where you can input your email content.

5. Type or paste your email content into the textarea provided.

6. Click the "Submit" button to classify the email.

7. The application will process the input and display the classification result below the form.

8. If the email is classified as spam, the result will be shown with the heading "SPAM" in red color (CSS class: one).

9. If the email is classified as not spam, the result will be shown with the heading "NOT SPAM" in green color (CSS class: two).

10. To reset the form and start over, you can click the "Reset" link.

## Customization

You can customize the Email Spam Classifier application by modifying the HTML template (index.html) and the CSS styles (style.css). Here are some possible customization options:

- Change the layout and design of the HTML template to match your preferred visual style.

- Modify the CSS styles to customize the appearance of the headings, form elements, and overall design.

- Add additional fields or features to the form, such as checkboxes or dropdown menus, to enhance the functionality of the application.

- Adjust the logic in the Flask application (app.py) to incorporate different machine learning models or preprocessing techniques.

## Deployment

To publish your web application on the web using Render.com, follow these steps:

### Prepare for publishing:

- Create a requirements.txt file listing all the libraries needed to run your Flask application using the command pip freeze > requirements.txt.

- I recommend updating the README.md file in your project folder to make it easier for others to understand what your repository is about.

### Push your changes to GitHub:

To execute the following instructions, you will need to open your terminal or command prompt and enter the following commands:

```python
git add . to stage all changes
git commit -m "Created email spam classifier"
git push origin main
```

If you're setting up git for the first time or facing issues while committing, you may need to do the git config setup.

### Publish with Render:

Go to the Render Dashboard and sign up or log in.

How to create a new deployment:
- Click on the "New" button and select "Web Services".
- Click on the "Connect with GitHub" button and choose your GitHub account.
- Give access to all your repositories or selected ones.
- Click "Install" after making your selection.
- Choose the repository you want to deploy.

On the final page of deployment, configure:

- A unique name for the web service.
- The region closest to you.
- The primary GitHub repository branch (usually "main").
- Ensure runtime is Python 3 and requirements.txt is configured correctly.
- The start command is gunicorn app:app (assuming your Flask object is initialized as app in the file app.py).
- Select your preferred instance type (Free instance for this tutorial).
- Click on "Create Web Service".

### Await deployment:

Wait for the deployment process to finish. It may take some time, especially with the free instance.
Address and fix any errors encountered during deployment.
Congratulations! Your deployed model is now live in production. For future changes, simply make the changes and push to your main branch on GitHub. Render will automatically deploy your changes.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License
The Email Spam Classifier project is licensed under the MIT License. You are free to use, modify, and distribute the code for personal or commercial purposes.