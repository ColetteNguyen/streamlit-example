import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

"""
# Welcome to the Facility Management chatbot!
"""

whatsapp_number = st.text_input('WhatsApp number')
mcst_number = st.text_input('MCST number')
name = st.text_input('Name')
phone_number = st.text_input('Phone number')
email = st.text_input('Email')
resident_unit_number = st.text_input('Resident Unit number')
agree = st.checkbox('I agree to the PDPC policy')
if st.button('Submit'):
    st.write('Thank you')



