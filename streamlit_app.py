import streamlit
import pandas

streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('๐ Omega 3 and & Blueberry Oatmeal')
streamlit.text('๐ฅฃ Kale, Spinach & Rocket Smoothie')
streamlit.text('๐ Hard-Boiled Free-Range Egg')
streamlit.text('๐ฅ๐ Avocado Tost')

streamlit.header('๐๐ฅญBuild Your Own Fruit smoothie๐ฅ๐')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(fruits_to_show)

streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

#fruityvice API request
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" +fruit_choice)
#streamlit.text(fruityvice_response.json())

# take the json version of the response and normalize it 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# output it the screen as table
streamlit.dataframe(fruityvice_normalized)

import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("Select * from fruit_load_list")
my_data_row = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_row)

streamlit.text("What fruit would you like to add?")
#my_data_row1 = my_cur.fetchone()
#streamlit.dataframe(my_data_row1)
streamlit.text("jackfruit")
streamlit.text("Thanks for adding jackfruit")

#This will not work correctly, but just go with it for now
my_cur.execute("insert into fruit_load_list values ('from streamlit')")
