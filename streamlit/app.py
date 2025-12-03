# UTF-8 Python 3.13.5
# Author: Intan K. Wardhani
# Last modified: 02-12-2025


import streamlit as st
from client import call_api
from utils import yes_no_to_binary

st.set_page_config(page_title="How much would you have to pay?", layout="centered")

st.title("Price Estimator for Belgian Real Estate")
st.write("Fill out the form below to estimate the property price.")

# ----------------------------
# 1. Model Selection
# ----------------------------
# make it default to XGBoost
# model_name = st.selectbox(
#     "Select Model",
#     ["Ridge", "RandomForest", "XGBoost"],
#     index=2
# )
model_name = "XGBoost"

# ----------------------------
# 2. Form Inputs (Categorical)
# ----------------------------
property_type = st.selectbox(
    "Property Type",
    ["Apartment", "House", "Master", "Duplex", "Triplex", "Penthouse", "Ground",
     "Student", "Studio",  
     "Bungalow", "Chalet", "Cottage", "Loft", "Mansion", "Residence", "Villa", 
     "Business", "Commercial", "Office", "Garage", "Development", "Land"]
)

building_state = st.selectbox(
    "Building State",
    ["Excellent", "Fully renovated", "New", "Normal", "To demolish", "To renovate", 
     "To restore", "Under construction"]
)

province = st.selectbox(
    "Province",
    ["Antwerp", "Brussels Capital Region", "East Flanders", "Flemish Brabant", "Hainaut", 
     "Liège", "Limburg", "Luxembourg", "Namur", "Walloon Brabant", "West Flanders"]
)

locality_name = st.text_input("Locality Name", "Brussels")

build_year_cat = st.selectbox(
    "Build Year Category",
    ["1800s", "1950s", "2020s"]
)

# ----------------------------
# 3. Numeric Inputs
# ----------------------------
living_area = st.number_input("Living Area (m²)", min_value=10.0, max_value=1000.0, value=100.0)
number_bedrooms = st.number_input("Number of Bedrooms", min_value=1.0, max_value=10.0, value=3.0)
postal_code = st.number_input("Postal Code", min_value=1000.0, max_value=9999.0, value=1000.0)
# build_year = st.number_input("Build Year", min_value=1800.0, max_value=2030.0, value=1990.0)
facades = st.selectbox("Number of Facades", [1, 2, 3, 4])

# ----------------------------
# 4. Yes/No Binary Inputs
# ----------------------------
swimming_pool = st.radio("Swimming Pool?", ["Yes", "No"])
garden = st.radio("Garden?", ["Yes", "No"])
terrace = st.radio("Terrace?", ["Yes", "No"])

# ----------------------------
# 5. Submit Button
# ----------------------------
if st.button("Predict Price"):
    payload = {
        # "build_year": build_year,
        "build_year_cat": build_year_cat,
        "building_state": building_state,
        "facades": facades,
        "garden": yes_no_to_binary(garden),
        "living_area": living_area,
        "locality_name": locality_name,
        "number_bedrooms": number_bedrooms,
        "postal_code": postal_code,
        "property_type": property_type,
        "province": province,
        "swimming_pool": yes_no_to_binary(swimming_pool),
        "terrace": yes_no_to_binary(terrace),
    }

    prediction = call_api(model_name, payload)

    if "error" in prediction:
        st.error(prediction["Sorry, an error occurred"])
    else:
        st.success(f"Estimated Price: **€{prediction['prediction']:,.0f}**")
