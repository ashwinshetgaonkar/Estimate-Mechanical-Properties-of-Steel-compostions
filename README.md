# Estimate-Mechanical-Properties-of-Steel-compostions

## Context
* Currently there are no precise theoretical methods to predict mechanical properties of steels. 
* All the methods available are by backed by statistics and extensive physical testing of the materials. 
* Since testing each material with different composition is a highly tedious task (imagine the number of possibilities!), let's apply our knowledge of machine learning and statistics to solve this problem.

## Data
* This dataset contains compositions by weight percentages of low-alloy steels along with the temperatures at which the steels were tested and the values mechanical properties observed during the tests. 
* The alloy code is a string unique to each alloy. Weight percentages of alloying metals and impurities like Aluminum, copper, manganese, nitrogen, nickel, cobalt, carbon, etc are given in columns.
*  The temperature in celsius for each test is mentioned in a column. 
*  Lastly mechanical properties including tensile strength, yield strength, elongation and reduction in area are given in separate columns. The dataset contains 915 rows.

## My work
* My aim for this Project is to analyse and transform the available data to make it fit to be used for model training.
* After that to use this data for building a model that accurately predicts the mechanical properties of steels.
* To achieve this I have first visualized the distribution of features and targets and transformed them so as to make them suitable for using in model training.
* I have further improved the performance of the model by tunning its hyperparameters using Optuna framework.
* To see the code along with the proper documentation check out [mech-prop-lightgbm-optuna.ipynb](https://github.com/ashwinshetgaonkar/Estimate-Mechanical-Properties-of-Steel-compostions/blob/main/mech-prop-lightgbm-optuna.ipynb)
* Deployed the best performing model using Streamlit.
* Tech stack used:Python, numpy, pandas, matplotlib, seaborn, lightgbm, optuna, streamlit, html, sklearn, scipy, joblib.


## Web app working:
* The user needs to enter the composition for which he/she wants to predict its mechanical properties and the application will compute the display the selected mechanical properties.
* To use the web app bulit using streamlit check out [app.py](https://share.streamlit.io/ashwinshetgaonkar/estimate-mechanical-properties-of-steel-compostions/main/app.py).


