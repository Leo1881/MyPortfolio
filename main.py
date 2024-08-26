import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/Lee.jpg")

with col2:
    st.title("Lee Johnson")
    content = """I'm Lee, a passionate graphic designer, Python programmer, and web developer with a keen eye for 
    aesthetics and a strong command of code. I blend creativity with technical expertise to craft visually stunning 
    designs, build dynamic websites, and develop efficient Python solutions. Dedicated to delivering high-quality 
    results that meet client needs and exceed expectations."""
    st.info(content)

content2 = """Below is a list of all my projects built using python. Feel free to contact me"""
st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"], width=300)
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"], width=300)
        st.write(f"[Source Code]({row['url']})")