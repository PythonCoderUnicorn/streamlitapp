import streamlit as st


st.header("Hello")

st.write("Hello Streamlit world!")

st.write(
    """
    # This is markdown title.
    this is some _markdown_
    """
)

import pandas as pd 

df = pd.DataFrame(
    {
        'col_1' : [1,2,3],
        'col_2': [4,5,6]
    }
)
st.write( df )


x = 10
st.write('x = ', x)

import numpy as np

n = np.random.randint(100)

'''
# Random Number
'''
st.write(n)