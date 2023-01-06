import streamlit
import pandas
import requests

streamlit.title('My Healthy Diner')
streamlit.header('Breakfast Favs')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')


streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
#fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),)
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),'Avocado')
fruits_to_show = my_fruit_list.loc[fruits_selected]
 
# Display the table on the page.
streamlit.dataframe(fruits_to_show)

#New section for fruityvice api response
streamlit.header("Fruityvice Fruit Advice!")

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json()) #shows the output on screen


#normalize data from pandas
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# add the normalized data into dataframe as a table
streamlit.dataframe(fruityvice_normalized)

