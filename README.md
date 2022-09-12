# Prediticting-Heart-Disease-using-Machine-Learning-Web-Application-


Find the Kaggle dataset here: https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset


1. Dataset Description: 

This data set dates from 1988 and consists of four databases: Cleveland, Hungary, Switzerland, and Long Beach V. It contains 13 features including the output feature labeled as “target”. There are a total of 1025 rows. Since this is a labeled dataset, it is a classification supervised dataset. Among the 13 features there are 5 numerical features, 7 categorical features and 1 output feature. The description of the dataset is given below:

Feature	Description	Range
age	- Age of person in years -	29-77
sex -	Gender of person -	0 = Female, 1 = Male
cp -	Chest pain type (Angina) -	0 = Typical, 1 = Atypical, 2 = non-Anginal, 3 = Asymptotic
trestbps -	Resting blood pressure -	94-200 mmHg
chol -	Serum Cholesterol level -	126-564 mg/dl
restecg -	Resting ECG -	0 = Normal, 1 = Abnormal, 2 = Hyper
thalach -	Maximum heart rate -	71-202 bpm
exang -	Exercise induced angina -	0 = No, 1 = Yes 
oldpeak -	ST depression induced by exercise relative to rest -	0-6.2 mmHg
slope -	Slope of the peak exercise ST segment -	0 = Up, 1=Flat, 2 = Down
ca -	Number of major vessels colored by fluoroscopy -	0-3
thal -	Thalassemia -	1 = Normal, 2 = Fixed defect, 3 = Reversible defect
target -	Heart disease or not -	0 = Does not have heart disease, 1 = Has heart disease

The numerical features of the dataset are age, trestbps, chol, thalach, oldpeak and the categorical features are sex, cp, restecg, exang, slope, ca, thal and the output feature is target. 

2.	Technology stack:

To make the predictive model and understand the dataset, we did exploratory data analysis where we figured out how to approach the prediction. In data pre-processing, a lot of visualizations were done. Later various data pre-processing techniques were used to make the dataset better for using predictive machine learning algorithms. At the end a pickle file was made from the best model in order to use it in the web application. The technical things used are as follows:

a)	Python
b)	Flask API
c)	HTML
d)	Bootstrap

The libraries that were used are as follows:

a)	Pandas
b)	Numpy
c)	Seaborn
d)	Matplotlib
e)	Scikit-Learn
f)	Plotly
g)	Pickle

3.	Model:

The best model came to Random Forest. We have used hyperparameters n_estimators and max_depth. Precision, Recall and F1 Score for no disease or 0 is 0.98, 0.91 and 0.94 respectively. Subsequently, for diseased or target features that are classified as 1, the precision, recall and F1 - score is 0.92, 0.98 and 0.95 respectively. The accuracy of random forest was 94.63%.

