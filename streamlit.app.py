
import streamlit as st
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

st.title ("My MOM's new healthy Dinner")
st.header('🥣 🥗 🐔 🥑🍞 Breakfast Menu 🥣 🥗 🐔 🥑🍞')
st.text('🥗 Curry Omega 3 & Blueberry Oatmeal')
st.text('🥑🍞 Sandwich Kale, Spinach & Rocket Smoothie')
st.text('🐔 Cooking Hard-Boiled Free-Range Egg')
st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected = st.multiselect("Pick Some Fruits", list(my_fruit_list.index),['Avocado','Strawberries'])

fruit_to_show = my_fruit_list.loc[fruits_selected]
st.dataframe(fruit_to_show)

st.header("Fruityvice Fruit Advice!")
try
    fruit_choice = st.text_input('What fruit would you like information about?)
 if not fruit_choice
    st.error('Please select a fruit to get information.')
 else
   fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+ fruit_choice)             
   fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
   st.dataframe(fruityvice_normalized)
                                 
 except URLError as e
    st.error()                             
#st.write('The user entered ', 'apple')

#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+ "apple")
#st.text(fruityvice_response.json()) # just write data to the screen
# write your own comment -what does the next line do? 
#fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
#st.dataframe(fruityvice_normalized)

st.stop();

my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("insert into fruit_load_list values ('from st')")
my_data_rows = my_cur.fetchall()
st.header("The Fruit Load List Contains:")
st.dataframe(my_data_rows)

add_my_fruit = st.text_input('What fruit would you like to add?','jackfruit')
st.write('The user entered ', add_my_fruit)

