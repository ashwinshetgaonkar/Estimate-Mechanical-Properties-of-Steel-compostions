# Estimate-Mechanical-Properties-of-Steel-compostions
This repository contains the code for predicting the Mechanical Properties of steels given its composition.


## About Dataset
### Context
Currently there are no precise theoretical methods to predict mechanical properties of steels. All the methods available are by backed by statistics and extensive physical testing of the materials. Since testing each material with different composition is a highly tedious task (imagine the number of possibilities!), let's apply our knowledge of machine learning and statistics to solve this problem.

### Content
This dataset contains compositions by weight percentages of low-alloy steels along with the temperatures at which the steels were tested and the values mechanical properties observed during the tests. The alloy code is a string unique to each alloy. Weight percentages of alloying metals and impurities like Aluminum, copper, manganese, nitrogen, nickel, cobalt, carbon, etc are given in columns. The temperature in celsius for each test is mentioned in a column. Lastly mechanical properties including tensile strength, yield strength, elongation and reduction in area are given in separate columns. The dataset contains 915 rows.

### Inspiration
The challenge is to predict the Mechanical properties using the alloy composition and temperature.

<hr>

### - To see the code along with the proper documentation check out [mech-prop-lightgbm-optuna.ipynb](https://github.com/ashwinshetgaonkar/Estimate-Mechanical-Properties-of-Steel-compostions/blob/main/mech-prop-lightgbm-optuna.ipynb)

### - To use the web app bulit using streamlit check out [app.py](https://share.streamlit.io/ashwinshetgaonkar/estimate-mechanical-properties-of-steel-compostions/main/app.py).

### - Tech stack used:Python, numpy, pandas, matplotlib, seaborn, lightgbm, optuna, streamlit, html, sklearn, scipy, joblib.
