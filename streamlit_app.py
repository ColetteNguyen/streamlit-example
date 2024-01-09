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

# Define required and optional fields
required_fields = ['WhatsApp number', 'MCST number', 'Resident Unit number', 'Name']
optional_fields = ['Email']

# Initialize session state
if 'form_data' not in st.session_state:
    st.session_state.form_data = {
        'whatsapp_number': '',
        'mcst_number': '',
        'resident_unit_number': '',
        'name': '',
        'email': '',
        'agree': False
    }

# Display input fields with labels indicating required and optional fields
whatsapp_number = st.text_input('WhatsApp number* (Required)', key='whatsapp_number', value=st.session_state.form_data['whatsapp_number'])
mcst_number = st.text_input('MCST number* (Required)', key='mcst_number', value=st.session_state.form_data['mcst_number'])
resident_unit_number = st.text_input('Resident Unit number* (Required)', key='resident_unit_number', value=st.session_state.form_data['resident_unit_number'])
name = st.text_input('Name* (Required)', key='name', value=st.session_state.form_data['name'])
email = st.text_input('Email (Optional)', key='email', value=st.session_state.form_data['email'])
agree = st.checkbox('I agree to the PDPC policy (Required)', key='agree', value=st.session_state.form_data['agree'])

submitted = False

if st.button('Submit'):
    # Check for required fields
    if not whatsapp_number or not mcst_number or not resident_unit_number or not name or not agree:
        st.warning('All required fields must be filled, and PDPC policy must be agreed to before submitting.')
    else:
        # Check if WhatsApp number already exists
        existing_record = collection.find_one({'whatsapp_number': whatsapp_number})

        if existing_record:
            st.warning(f'The WhatsApp number {whatsapp_number} already exists. You can use the chatbot.')
        else:
            form_data = {
                'role': 'resident',
                'phone_number': whatsapp_number,
                'mcst_no': mcst_number,
                'resident_unit_number': resident_unit_number,
                'name': name,
                'email': email,
            }

            collection.insert_one(form_data)

            # Display a success message in a popup
            st.success('Data submitted successfully! Now, you can use the chatbot.')

            # Manually reset form fields after successful submission
            st.session_state.form_data = {
                'whatsapp_number': '',
                'mcst_number': '',
                'resident_unit_number': '',
                'name': '',
                'email': '',
                'agree': False
            }

            submitted = True

