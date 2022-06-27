import streamlit as st
import time
import numpy as np
from sorts import *
import random

def generate(n):
    t = [0]*n
    for i in range(n):
        t[i] = random.randint(1,200)
    return t

st.set_page_config(layout='wide')

with st.sidebar:
    t = st.slider('Pick a delay (ms)', 0, 1000) / 1000
    y = st.slider('Pick a number', 10, 200)
    sort_type = st.radio("Pick a sorting algorithm", ('Bubble Sort', 'Insertion Sort', 'Selection Sort', 'Cycle Sort', 'Merge Sort', 'Heap Sort', "Quick Sort"))
    text = st.empty()
    st.text("Worst case")
    wruntime = st.latex(r[sort_type])
    st.text("Average case")
    aruntime = st.latex(a[sort_type])
    

placeholder = st.empty()
x = generate(y)
placeholder.bar_chart(x)
title = st.header(sort_type)
subtitle = st.subheader(s[sort_type])

paragraph = st.text(p[sort_type])

with st.sidebar:
    if st.button('Start sort'):
        text.text("Sorting")
        d[sort_type](x, placeholder, t)
        text.text("Sorted!")
    
