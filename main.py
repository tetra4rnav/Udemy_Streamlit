import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 超入門')

st.write('Progress Bar')
'FUCK OFF'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

# option = st.selectbox(
#     'ちいかわは好き度は？',
#     list(range(1, 11))
# )

# 'ちいかわ好き度は', option, 'だって？'

# option = st.text_input('きみは何？')
# 'きみは', option,  'だって？'

# option = st.slider('あなたは何%ちいかわ？', 0, 100, 50)
# 'ちいかわ度：', option, '%'


# left_columns, right_columns = st.columns(2)
# button = left_columns.button('右カラムを見る')
# if button:
#     right_columns.write('こんちわ')

expander = st.expander('問い合わせ')
expander.write('何？')