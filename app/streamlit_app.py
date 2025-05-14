import streamlit as st
import requests
# At the top of the file or just before the form:
if "reset_triggered" not in st.session_state:
    st.session_state.reset_triggered = False

# --- Reset button at the bottom ---
if st.button("🔄 Reset Form"):
    st.session_state.clear()
    st.session_state.reset_triggered = True
    st.rerun()

with st.form("rent_form"):
    city = st.selectbox("City", ["", "Nagpur"], index=0)
    area = st.text_input("Area", "")
    location = st.text_input("Location", "")
    location_hub = st.selectbox(
        "Location Hub", 
        ["", "Retail Complex/ Building", "business park", "others", "commercial project", "Market/ High Street", "IT Park"], 
        index=0
    )
    zone = st.selectbox("Zone", ["", "East", "West", "North", "South"], index=0)
    property_type = st.selectbox("Property Type", ["", "Office", "Shop", "Showroom", "Warehouse"], index=0)
    ownership = st.selectbox("Ownership", ["", "Freehold", "Leasehold", "Rented"], index=0)
    size_in_sqft = st.number_input("Size (in sqft)", min_value=0, value=0)
    carpet_area_sqft = st.number_input("Carpet Area (in sqft)", min_value=0, value=0)
    private_washroom = st.selectbox("Private Washroom", ["", "Yes", "No"], index=0)
    public_washroom = st.selectbox("Public Washroom", ["", "Yes", "No"], index=0)
    electric_charge_included = st.selectbox("Electricity Charges Included", ["", "Yes", "No"], index=0)
    water_charge_included = st.selectbox("Water Charges Included", ["", "Yes", "No"], index=0)
    property_age = st.selectbox("Age of Property", ["", "0-1 years", "1-5 years", "5-10 years", "10+ years"], index=0)
    possession_status = st.selectbox("Possession Status", ["", "Immediate", "Within 3 Months", "After 3 Months"], index=0)
    posted_by = st.selectbox("Posted By", ["", "Owner", "Agent", "Builder"], index=0)
    rent_increase_per_year = st.selectbox("Yearly Rent Increase", ["", "0%", "5%", "10%", "15%"], index=0)
    negotiable = st.selectbox("Rent Negotiable", ["", "Yes", "No"], index=0)
    brokerage = st.selectbox("Brokerage Applicable", ["", "Yes", "No"], index=0)
    floor_no = st.selectbox("Floor Number", ["", "Ground", "1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "9th", "10th", "11th", "12th"], index=0)
    total_floors = st.selectbox("Total Floors in Building", [""] + [str(i) for i in range(1, 13)], index=0)
    amenities_count = st.selectbox("Number of Amenities", [""] + [str(i) for i in range(1, 16)], index=0)

    submitted = st.form_submit_button("Predict Rent")
