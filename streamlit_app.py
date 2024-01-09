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

whatsapp_number = st.text_input('WhatsApp number')
mcst_number = st.text_input('MCST number')
resident_unit_number = st.text_input('Resident Unit number')
name = st.text_input('Name')
email = st.text_input('Email')
agree = st.checkbox('I agree to the PDPC policy')

if st.button('Submit'):
    # Check if the user has agreed to the policy
    if not agree:
        st.warning('Please agree to the PDPC policy before submitting.')
    else:
        # Create a dictionary with the form data
        form_data = {
            'role': 'resident,
            'phone_number': whatsapp_number,
            'mcst_no': mcst_number,
            'resident_unit_number': resident_unit_number,
            'name': name,
            'email': email
        }

        # Insert the data into MongoDB
        collection.insert_one(form_data)

        # Display a success message
        st.success('Data submitted successfully!')

# Optional: Display the data in a table for verification
st.subheader('Submitted Data:')
data = list(collection.find())
df = pd.DataFrame(data)
st.table(df)
