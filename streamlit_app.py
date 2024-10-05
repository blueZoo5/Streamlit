import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.title('Streamlit for sin and cos functional visulalization')

x_start = st.slider('x', 0.0, 10.0, 0.0)
x_end = st.slider('x', 10.0, 20.0, 10.0)

x = np.linspace(x_start, x_end)

print(x)

y_sin = np.sin(x)
y_cos = np.cos(x)

fig, ax = plt.subplots()

ax.plot(x, y_sin)
ax.plot(x, y_cos)
ax.legend(['sin', 'cos'])
ax.set_xlabel('x-axis')
ax.set_ylabel('y-axis')

ax.set_title('sin and cos function')

st.pyplot(fig)
