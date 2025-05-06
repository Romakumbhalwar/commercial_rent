import streamlit as st
import requests

# Set the page configuration
st.set_page_config(page_title="Commercial Rent Predictor", layout="centered")

st.title("🏢 Commercial Property Rent Prediction")

# FastAPI endpoint URL
API_URL = "https://commercial-rent-model.onrender.com/predict"

# Resetting all session state on page load (to clear any old data)
if "predicted_rent" in st.session_state:
    del st.session_state["predicted_rent"]

# User input form
with st.form("rent_prediction_form"):
    st.subheader("Enter Property Details")

    # Input fields for property details
    city = st.text_input("City", value="")
    area = st.text_input("Area", value="")
    location = st.text_input("Location", value="")
    zone = st.text_input("Zone", value="")
    location_hub = st.selectbox("Location Hub", ["Yes", "No"], index=0)
    property_type = st.selectbox("Property Type", ["Office", "Shop", "Showroom", "Warehouse"], index=0)
    ownership = st.selectbox("Ownership", ["Freehold", "Leasehold"], index=0)
    size_in_sqft = st.number_input("Size in Sqft", min_value=0.0, value=0.0)
    carpet_area_sqft = st.number_input("Carpet Area in Sqft", min_value=0.0, value=0.0)
    private_washroom = st.selectbox("Private Washroom", ["Yes", "No"], index=0)
    public_washroom = st.selectbox("Public Washroom", ["Yes", "No"], index=0)
    floor_no = st.text_input("Floor No (e.g. Ground, 1st, Basement)", value="")
    total_floors = st.text_input("Total Floors", value="")
    amenities_count = st.number_input("Number of Amenities", min_value=0, value=0)
    electric_charge_included = st.selectbox("Electricity Charges Included?", ["Yes", "No"], index=0)
    water_charge_included = st.selectbox("Water Charges Included?", ["Yes", "No"], index=0)
    property_age = st.text_input("Property Age (e.g. 5-10 years, New)", value="")
    possession_status = st.selectbox("Possession Status", ["Immediate", "Under Construction"], index=0)
    posted_by = st.selectbox("Posted By", ["Owner", "Dealer", "Builder"], index=0)
    rent_increase_per_year = st.selectbox("Rent Increase Per Year", ["Yes", "No"], index=0)
    negotiable = st.selectbox("Rent Negotiable?", ["Yes", "No"], index=0)
    brokerage = st.selectbox("Brokerage", ["Yes", "No"], index=0)

    submit = st.form_submit_button("Predict Rent")

if submit:
    # Collecting input data
    input_data = {
        "city": city,
        "area": area,
        "location": location,
        "zone": zone,
        "location_hub": location_hub,
        "property_type": property_type,
        "ownership": ownership,
        "size_in_sqft": size_in_sqft,
        "carpet_area_sqft": carpet_area_sqft,
        "private_washroom": private_washroom,
        "public_washroom": public_washroom,
        "floor_no": floor_no,
        "total_floors": total_floors,
        "amenities_count": amenities_count,
        "electric_charge_included": electric_charge_included,
        "water_charge_included": water_charge_included,
        "property_age": property_age,
        "possession_status": possession_status,
        "posted_by": posted_by,
        "rent_increase_per_year": rent_increase_per_year,
        "negotiable": negotiable,
        "brokerage": brokerage
    }

    with st.spinner("Getting prediction..."):
        try:
            # Sending data to FastAPI for prediction
            response = requests.post(API_URL, json=input_data)
            if response.status_code == 200:
                rent = response.json()["predicted_rent"]
                st.session_state["predicted_rent"] = rent
                st.success(f"Estimated Rent: ₹ {rent:.2f} per month")
            else:
                st.error("❌ Server error: Could not get prediction.")
        except Exception as e:
            st.error(f"🚫 Request failed: {e}")

# To make sure old recommendations are not displayed:
if "predicted_rent" in st.session_state:
    st.write(f"Last predicted rent: ₹ {st.session_state['predicted_rent']:.2f}")
