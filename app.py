import streamlit as st
import pandas as pd
import openpyxl

# Load the dataset

df = pd.read_excel('drone_metadata.xlsx', engine='openpyxl')

# Streamlit app title
st.title("Drone Metadata Viewer")

# Dropdown menu for selecting metadata item
metadata_items = df['Drone Data Record Items'].dropna().tolist()
selected_item = st.selectbox("Select a Drone Data Record Item", metadata_items)

details = df[df['Drone Data Record Items'] == selected_item]
if not details.empty:
    section = details['Sections'].values[0]
    source = details['Source'].values[0]
    
    st.write(f"**Section:** {section}")
    st.write(f"**Source:** {source}")
else:
    st.write("No details available.")
