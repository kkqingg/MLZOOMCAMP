# MLZOOMCAMP
This is the midterm project of this course using a titanic dataset. LogisticRegression algorithm is used . The model is uploaded into a flask web service and deploy it locally with Docker

"Dockerfile" contains all the images and necessary dev applications

"load.py" This python file contains initiating a flask web service by linking with the model and building the app.

"midterm_titanic.py" This python file contains the dataset, data cleaning, pre-processing , model training, 
model prediction and export model into a .bin file using pickle.

"real.py" This python file contains the a dict type sample to test the model and request that sample data to 
join to the url and see the result. 

"Pipfile" and "Pipfile.lock" contains the exact versions of the necessary apps such as scikit-learn, 
numpy and flask

"model_C=logisticmodel.bin" is a file of the ML model. 


