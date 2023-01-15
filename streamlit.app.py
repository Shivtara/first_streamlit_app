
import streamlit as st
st.title ("My MOM's new healthy Dinner")
st.header('🥣 🥗 🐔 🥑🍞 Breakfast Menu 🥣 🥗 🐔 🥑🍞')
st.text('🥗 Curry Omega 3 & Blueberry Oatmeal')
st.text('🥑🍞 Sandwich Kale, Spinach & Rocket Smoothie')
st.text('🐔 Cooking Hard-Boiled Free-Range Egg')
st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected = st.multiselect("Pick Some Fruits", list(my_fruit_list.index),['Avocado','Strawberries'])

fruit_to_show = my_fruit_list.loc[fruits_selected]
st.dataframe(fruit_to_show)

st.header("Fruityvice Fruit Advice!")
fruit_choice = st.text_input('What fruit would you like information about?','apple')
st.write('The user entered ', 'apple')
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+ "apple")
#st.text(fruityvice_response.json()) # just write data to the screen
# write your own comment -what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
st.dataframe(fruityvice_normalized)


import snowflake.connector
