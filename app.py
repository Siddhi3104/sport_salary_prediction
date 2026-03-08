from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

with open('model.pkl', 'rb') as f:
    regression_model = pickle.load(f)

with open('classifier.pkl', 'rb') as f:
    classification_model = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():

    age = int(request.form['age'])
    experience = int(request.form['experience'])
    matches_played = int(request.form['matches_played'])
    total_runs = int(request.form['total_runs'])
    performance_rating = float(request.form['performance_rating'])

    features = np.array([[age, experience, matches_played, total_runs, performance_rating]])

    predicted_salary = regression_model.predict(features)[0]

    salary_category = classification_model.predict(features)[0]
    
   
    r2_accuracy = 0.98 
    classification_accuracy = 1.00  

    return render_template('index.html', 
                           predicted_salary=f'{predicted_salary:,.2f}', 
                           salary_category=salary_category,
                           r2_accuracy=f'{r2_accuracy:.2f}',
                           classification_accuracy=f'{classification_accuracy:.2f}')

if __name__ == '__main__':
    app.run(debug=True)
