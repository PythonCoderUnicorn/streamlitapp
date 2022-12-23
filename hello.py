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



import streamlit as st
import numpy as np
import pandas as pd

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)





import streamlit as st
x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)



company = {
    'income': 120_000,
    'expenses': 78_900
}

def net_income( dict ):
    net = dict['income'] - dict['expenses']
    st.write(f"Net income = ${.2f}".format(net))


net_income(company)