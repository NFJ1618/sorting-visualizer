import streamlit as st
import time
import numpy as np
from sorts import *
import random

def generate(n):
    t = [0]*n
    for i in range(n):
        t[i] = random.randint(0,1000)
    return t

st.set_page_config(layout='wide')

with st.sidebar:
    t = st.slider('Pick a delay (ms)', 0, 1000) / 1000
    y = st.slider('Pick a number', 10, 200)
    sort_type = st.radio("Pick a sorting algorithm", ('Bubble Sort', 'Insertion Sort', 'Selection Sort', 'Cycle Sort', 'Merge Sort', 'Heap Sort', "Quick Sort"))
    text = st.empty()

placeholder = st.empty()
x = generate(y)
placeholder.bar_chart(x)

with st.sidebar:
    if st.button('Start sort'):
        text.text("Sorting")
        d[sort_type](x, placeholder, t)
        text.text("Sorted!")
    
