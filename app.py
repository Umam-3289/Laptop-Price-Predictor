import streamlit as st
import pandas as pd
import numpy as np
import pickle

pipe=pickle.load(open('pipe.pkl','rb'))
df=pickle.load(open('df.pkl','rb'))

st.title("Laptop Price Predictor")

#brand
Company=st.selectbox('Brand',df['Company'].unique())

#type
type=st.selectbox('Type',df['TypeName'].unique())

#Ram
ram=st.selectbox('RAM(in GB)',[2,4,6,8,12,16,24,32,64])

#weight
weight=st.number_input('Weight of the Laptop')

#Touchscreen
touchscreen=st.selectbox('Touhscreen',['No','Yes'])

#IPS
ips=st.selectbox('IPS',['No','Yes'])

#screen size
screen_size=st.number_input('Screen Size')

#resolution
resolution = st.selectbox('Screen Resolution',
['1920x1080','1366x768','1600x900','3840x2160',
'3200x1800','2880x1800','2560x1600','2560x1440','2304x1440'])

#CPU
cpu=st.selectbox('Brand',df['CPU Brand'].unique())
hdd=st.selectbox('HDD(in GB)',[0,128,256,512,1024,2048])
ssd=st.selectbox('SSD(in GB)',[0,128,256,512,1024])
gpu=st.selectbox('GPU',df['GPU Brand'].unique())
os=st.selectbox('OS',df['OS'].unique())

if st.button('Predict Price'):
    touchscreen = 1 if touchscreen == 'Yes' else 0
    ips = 1 if ips == 'Yes' else 0
    x_res = int(resolution.split('x')[0])
    y_res = int(resolution.split('x')[1])
    ppi = ((x_res**2 + y_res**2)**0.5) / screen_size

    # Create DataFrame for model input
    query = pd.DataFrame([[Company, type, ram, weight, touchscreen, ips, ppi, cpu, hdd, ssd, gpu, os]],
                         columns=['Company', 'TypeName', 'Ram', 'Weight', 'TouchScreen', 'IPS', 'PPI',
                                  'CPU Brand', 'HDD', 'SSD', 'GPU Brand', 'OS'])

    # Predict
    predicted_price = int(np.exp(pipe.predict(query)[0]))
    st.success(f"The Predicted Price of this configuration is ₹ {predicted_price}")
