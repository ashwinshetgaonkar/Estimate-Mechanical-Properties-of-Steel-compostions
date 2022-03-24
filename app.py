import pandas as pd
import numpy as np
import joblib
import streamlit as st
from scipy import stats

st.markdown('## Estimating Mechanical Properties of Steels')
st.markdown("---")


skew_cols=[' C', ' Si', ' Mn', ' P', ' S', ' Ni', ' Cr', ' Mo', ' Cu', 'V', ' Al', 'Ceq', 'Nb + Ta']

inputs={}

allow_code_list=['MBB', 'MBC', 'MBD', 'MBE', 'MBF', 'MBG', 'MBH', 'MBJ', 'MBL',
       'MBM', 'MBN', 'CAA', 'CAB', 'CAC', 'CAG', 'CAH', 'CAJ', 'CAL',
       'CAM', 'CAN', 'LAA', 'LAB', 'LAC', 'LAD', 'LAE', 'LAF', 'LAG',
       'LAH', 'LAJ', 'LAL', 'LAM', 'LAN', 'CaC', 'CaD', 'CaE', 'CaF',
       'CaG', 'CaH', 'CaM', 'CaN', 'VaA', 'VaB', 'VaC', 'VaD', 'VaE',
       'VaG', 'VaH', 'Vaj', 'VaR', 'LaA', 'LaB', 'LaD', 'LaE', 'LaF',
       'MFA', 'MFB', 'MFD', 'MFE', 'MFF', 'MFG', 'MFH', 'MFL', 'MFM',
       'VbA', 'VbB', 'VbD', 'VbF', 'VbG', 'VbH', 'VbJ', 'VbM', 'VbN',
       'CbA', 'CbB', 'CbC', 'CbD', 'CbE', 'CbF', 'CbG', 'CbH', 'CbJ',
       'CbL', 'CbM', 'CbN', 'CbR', 'CbS', 'CbT', 'CbU', 'CbV', 'CbW',
       'CbX', 'CbY', 'CbZ', 'CCA', 'CCB']

alloy_code_cat_codes=[57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67,  0,  1,  2,  3,  4,  5,
        6,  7,  8, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 11, 12,
       13, 14, 15, 16, 17, 18, 77, 78, 79, 80, 81, 82, 83, 85, 84, 52, 53,
       54, 55, 56, 68, 69, 70, 71, 72, 73, 74, 75, 76, 86, 87, 88, 89, 90,
       91, 92, 93, 94, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31,
       32, 33, 34, 35, 36, 37, 38, 39,  9, 10]


st.markdown("### Inputs:")
st.markdown("---")
inputs['alloy_code'] = st.selectbox(
     'Alloy code:',
     allow_code_list)
pos=allow_code_list.index(inputs['alloy_code'])
inputs['alloy_code']=alloy_code_cat_codes[pos]
# st.write('You selected:', inputs['alloy_code'])


st.write(" ")


inputs[' C']=st.slider('Select the composition of Carbon:', 0.09, 0.34, 0.17)
# st.write('You selected:', inputs[' C'])

st.write(" ")




inputs[' Si']=st.slider('Select the composition of Silicon:', 0.18, 0.52, 0.31)
# st.write('You selected:', inputs[' Si'])
st.write(" ")


inputs[' Mn']=st.slider('Select the composition of Manganese:', 0.42, 1.48, 0.81)
# st.write('You selected:', inputs[' Mn'])
st.write(" ")

inputs[' P']=st.slider('Select the composition of Phosphorus:', 0.006, 0.03, 0.014)
# st.write('You selected:', inputs[' P'])
st.write(" ")




inputs[' S']=st.slider('Select the composition of Sulphur:', 0.003, 0.022, 0.011)
# st.write('You selected:', inputs[' S'])
st.write(" ")

inputs[' Ni']=st.slider('Select the composition of Nickel:', 0.000, 0.6, 0.143)
# st.write('You selected:', inputs[' Ni'])
st.write(" ")

inputs[' Cr']=st.slider('Select the composition of Chromium:', 0.000, 1.31, 0.427)
# st.write('You selected:', inputs[' Cr'])
st.write(" ")


inputs[' Mo']=st.slider('Select the composition of Molybdenum:', 0.005, 1.35, 0.442)
# st.write('You selected:', inputs[' Mo'])
st.write(" ")

inputs[' Cu']=st.slider('Select the composition of Copper:', 0.000, 0.25, 0.079)
# st.write('You selected:', inputs[' Cu'])
st.write(" ")

inputs['V']=st.slider('Select the composition of Vanadium:', 0.000, 0.3, 0.06)
# st.write('You selected:', inputs['V'])
st.write(" ")


inputs[' Al']=st.slider('Select the composition of Aluminium:', 0.002, 0.05, 0.012)
# st.write('You selected:', inputs[' Al'])
st.write(" ")




inputs[' N']=st.slider('Select the composition of Nitrogen:', 0.002,0.015,0.007)
# st.write('You selected:', inputs[' N'])
st.write(" ")


inputs['Ceq']=st.slider('Select the value of Carbon Equivalent:', 0.000,0.437,0.093)
# st.write('You selected:', inputs['Ceq'])
st.write(" ")

inputs['Nb + Ta']=st.slider('Select the composition of Geochemical Twins(Nb+Ta):', 0.000,0.0017,0.000)
# st.write('You selected:', inputs['Nb + Ta'])
st.write(" ")


inputs['Temp']=st.number_input('Enter the value of Temperature in (`C):',27)
# st.write('You selected:', inputs['Temp'])
st.write(" ")




lambda_values=[-9.068636352260029,
 -4.875651063150875,
 -2.1073766019718567,
 -49.17492503823168,
 -65.10538144758746,
 -5.977314621505173,
 -1.6642711204766896,
 -0.6196430111399688,
 -9.32760990979712,
 -14.186091582934434,
 -84.53109579769365,
 -11.772744583758996,
 -24486.02947211213]
for col,lam in zip(skew_cols,lambda_values):
       inputs[col]=(pow(inputs[col]+1,lam)-1)/lam

# for col in skew_cols:
#        print(inputs[col])
#
input_values=[]
keys=[]
for k,v in inputs.items():
    keys.append(k)
    input_values.append(v)

# st.write(keys,input_values)


st.markdown('---')
options = st.multiselect(
     'Choose the Properties you want to Predict:',
     ['Proof Stress', 'Tensile Stress', '% Elongation', '% Reduction in Area'])

# st.write('You selected:', options)
st.write(" ")

if 'Proof Stress' in options:
    model=joblib.load('model_to_predict_proof_stress.pkl')
    prediction=model.predict([input_values])
    prediction=np.round(np.expm1(prediction),4)

    st.write("Proof Stress:",prediction[0],"MPa")

if 'Tensile Stress' in options:
    model=joblib.load('model_to_predict_tensile_stress.pkl')
    prediction=model.predict([input_values])
    prediction=np.round(np.expm1(prediction),4)

    st.write("Tensile Stress:",prediction[0],"MPa")


if '% Elongation' in options:
    model=joblib.load('model_to_predict_%elongation_stress.pkl')
    prediction=model.predict([input_values])
    prediction=np.round(np.expm1(prediction),2)
    st.write("% Elongation:",prediction[0],'%')


if '% Reduction in Area' in options:
    model=joblib.load('model_to_predict_%_redn_in_area.pkl')
    prediction=model.predict([input_values])
    prediction=np.round(np.expm1(prediction),2)

    st.write("% Reduction in Area:",prediction[0],'%')

st.markdown('---')
