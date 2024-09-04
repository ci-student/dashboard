import streamlit as st  # Importing the Streamlit library
from app_pages.multi_page import MultiPage  # Importing the MultiPage class from app_pages.multi_page module

from app_pages.dashboard import dashboard_body  # Importing the calculator_body function from app_pages.page_calculator module

app = MultiPage(app_name="Dashboard App")  # Creating an instance of the MultiPage class with the app name "Calculator App"

app.add_page("Insurance", dashboard_body)  # Adding a page named "Calculator" with the calculator_body function as its content

app.run()  # Running the MultiPage app