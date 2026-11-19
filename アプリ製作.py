import streamlit as st
st.title("食べたもの記録")
st.write("これから作品を作っていきます。")

text=st.text_input("あなたの名前は？")
st.write("あなたな名前は、"+text+"です")

condition=st.slider("今の調子は？",0,100,50)
#最小値、最大値、スタート位置
st.write("コンディション：",condition)

option=st.selectbox("好きな数字を教えろ",list(["1","10","100","1000"]))
st.write("あなたが選択したのは"+option+"です")

left_column,right_column=st.columns(2)
button=left_column.button("右カラムに文字を表示")
if button:
    right_column.write("ここは右カラムですけどなにか？")

from PIL import Image
img = Image.open("IMG_0092.jpg")
st.image(img,caption="かぶとむし")

import pandas as pd
import numpy as np
df=pd.DataFrame(
    np.random.rand(100,2)/[50,50] + [36.64,138.19],
     columns=["lat","lon"]
)
st.map(df)
st.table(df)
st.bar_chart(df)