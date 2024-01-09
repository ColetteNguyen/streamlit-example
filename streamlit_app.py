import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import pymongo

CONNECTION_STRING = "mongodb+srv://colette:6xUTl6YRSY8mHoaK@telegrambot.zulss7f.mongodb.net/test"
client = pymongo.MongoClient(CONNECTION_STRING)
dbname = client['new_facility_booking']
collection = dbname["roles"]

"""
# Welcome to the Facility Management chatbot!
"""
# Display input fields with labels indicating required and optional fields
whatsapp_number = st.text_input('WhatsApp number* (Required)')
mcst_number = st.text_input('MCST number* (Required)')
resident_unit_number = st.text_input('Resident Unit number* (Required)')
name = st.text_input('Name* (Required)')
email = st.text_input('Email (Optional)')
agree = st.checkbox('I agree to the PDPC policy')

if st.button('Submit'):
    if not whatsapp_number or not mcst_number or not resident_unit_number or not name:
        st.warning('All fields are required.')
    elif not agree:
        st.warning('Please agree to the PDPC policy before submitting.')
    else:
        form_data = {
            'role': 'resident',
            'phone_number': whatsapp_number,
            'mcst_no': mcst_number,
            'resident_unit_number': resident_unit_number,
            'name': name,
            'email': email
        }

        collection.insert_one(form_data)

        # Display a success message in a popup
        st.success('Data submitted successfully!')
        st.write('Thank you')

# Reset form fields after successful submission
whatsapp_number = ""
mcst_number = ""
resident_unit_number = ""
name = ""
email = ""
agree = False



