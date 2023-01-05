
import streamlit as st
st.title ('My MOM\s new healthy Dinner')
st.header('🥣 🥗 🐔 🥑🍞 Breakfast Menu 🥣 🥗 🐔 🥑🍞')
st.text('🥗 Curry Omega 3 & Blueberry Oatmeal')
st.text('🥑🍞 Sandwich Kale, Spinach & Rocket Smoothie')
st.text('🐔 Cooking Hard-Boiled Free-Range Egg')
st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# let's put pick list
my_fruit_list = my_fruit_list.set.index('Fruit')

st.multiselect("Pick Some Fruits", list(my_fruit_list.index))

st.dataframe(my_fruit_list)
