import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
from pymongo import MongoClient

"""
# Welcome to the Facility Management chatbot!
"""
CONNECTION_STRING = "mongodb+srv://colette:6xUTl6YRSY8mHoaK@telegrambot.zulss7f.mongodb.net/test"
client = MongoClient(CONNECTION_STRING)
dbname = client['realtimme_chatbot']
collection = dbname["vms"]



