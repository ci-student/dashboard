import streamlit as st  # Importing the Streamlit library
from app_pages.multi_page import MultiPage  # Importing the MultiPage class from app_pages.multi_page module
from app_pages.dashboard import dashboard_body 
 
app = MultiPage(app_name="Dashboard App")  
app.add_page("Insurance", dashboard_body)

app.run()  # Running the MultiPage app