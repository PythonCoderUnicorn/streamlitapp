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




st.markdown('Streamlit is **_really_ cool**.')
st.markdown(' This text is :red[colored red], and this is **:blue[colored]** and bold.')
st.markdown(":green[$\sqrt{x^2+y^2}=1$] is a Pythagorean identity. :pencil:")