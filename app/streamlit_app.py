import streamlit as st
import requests

st.set_page_config(page_title="Commercial Rent Predictor", layout="centered")

st.title("🏢 Commercial Property Rent Prediction")
st.write("Enter the property details below to get the estimated monthly rent:")

with st.form("rent_form"):
    city = st.selectbox("City", ["Nagpur"])
    area = st.text_input("Area")
    location = st.text_input("Location")
    zone = st.text_input("Zone")
    location_hub = st.selectbox("Location Hub", ["Retail Complex/ Building","business park","others","commercial project","Market/ High Street","IT Park"])
    property_type = st.selectbox("Property Type", ["Office", "Shop", "Showroom"])
    ownership = st.selectbox("Ownership", ["Freehold", "Leasehold", "Rented"])
    size_in_sqft = st.number_input("Size (in sqft)", min_value=100)
    carpet_area_sqft = st.number_input("Carpet Area (in sqft)", min_value=50)
    private_washroom = st.selectbox("Private Washroom", ["Yes", "No"])
    public_washroom = st.selectbox("Public Washroom", ["Yes", "No"])
    electric_charge_included = st.selectbox("Electricity Charges Included", ["Yes", "No"])
    water_charge_included = st.selectbox("Water Charges Included", ["Yes", "No"])
    property_age = st.selectbox("Age of Property", ["0-1 years", "1-5 years", "5-10 years", "10+ years"])
    possession_status = st.selectbox("Possession Status", ["Immediate", "Within 3 Months", "After 3 Months"])
    posted_by = st.selectbox("Posted By", ["Owner", "Agent", "Builder"])
    rent_increase_per_year = st.selectbox("Yearly Rent Increase", ["0%", "5%", "10%", "15%"])
    negotiable = st.selectbox("Rent Negotiable", ["Yes", "No"])
    brokerage = st.selectbox("Brokerage Applicable", ["Yes", "No"])
    
    # Fixed or calculated fields
    floor_no = "5th"
    total_floors = "10"
    amenities_count = 5  # Change if needed

    submitted = st.form_submit_button("Predict Rent")

    if submitted:
        payload = {
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

        try:
            response = requests.post("http://localhost:8000/predict", json=payload)
            if response.status_code == 200:
                predicted_rent = response.json()["predicted_rent"]
                st.success(f"💰 Predicted Monthly Rent: ₹{int(predicted_rent):,}")
            else:
                st.error(f"❌ Prediction failed. Server responded with status code {response.status_code}: {response.text}")
        except Exception as e:
            st.error(f"🚫 Error connecting to prediction API: {e}")
