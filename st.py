import streamlit as st
from keras.models import load_model
import matplotlib.pyplot as plt
from PIL import Image
import cv2

model=load_model('weights_bestv5.hdf5')
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:  
    st.write(uploaded_file)
    print(uploaded_file)
