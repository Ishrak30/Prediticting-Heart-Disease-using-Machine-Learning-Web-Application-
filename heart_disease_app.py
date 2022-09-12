import numpy as np
import pickle
from flask import Flask, request, render_template


model = pickle.load(open(
    'D:/NSU COURSES/NSU SEMESTER 14/CSE445/Model Work/Webapp Main/Main Web Heart/eda-pickle.pkl', 'rb'))


app = Flask(__name__)

# home


@app.route('/')
def home():
    return render_template('Heart Disease Classifier.html')

# predict


@app.route('/predict', methods=['POST'])
def predict():

    # Put all form entries values in a list
    features = [float(i) for i in request.form.values()]
    # Convert features to array
    array_features = [np.array(features)]
    print(array_features)
    # Predict features
    prediction = model.predict(array_features)
    print(prediction)

    #output = prediction

    # Output
    if prediction == 1:
        return render_template('Heart Disease Classifier.html',
                               result='The patient is very likely to have heart disease!')
    else:
        return render_template('Heart Disease Classifier.html',
                               result='The patient is unlikely to have heart disease!')


if __name__ == '__main__':
    app.run()
