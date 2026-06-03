import streamlit as st
import pandas as pd
import numpy as np
import os
import pickle

st.set_page_config(page_title = "Smart Hospital Patient Navigator" page_icon = "🏥", layout = "wide")

st.markdown("""
<style>
@import url ('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

html, body, [class*="css"] {font-family:'Inter', sans-serif;}
