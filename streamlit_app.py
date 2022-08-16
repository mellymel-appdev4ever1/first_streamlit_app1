print('Hello, World!')
import streamlit
streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.header('Breakfast Favorites')
streamlit.text('🥣Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avovado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.multiselect("Pick some fruits:", list(my_fruits_list.index))
streamlit.dataframe(my_fruit_list)

