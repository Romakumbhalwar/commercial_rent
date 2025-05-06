import streamlit as st
import requests

st.title("Commercial Rent Prediction")

st.subheader("Enter Property Details")

# Input fields
input_data = {
    "city": st.text_input("City", "nagpur"),
    "area": st.text_input("Area", "manewada"),
    "location": st.text_input("Location", "manewada,nagpur"),
    "zone": st.selectbox("Zone", ["north", "south", "east", "west"]),
    "location_hub": st.text_input("Location Hub", "Tech Park"),
    "property_type": st.selectbox("Property Type", ["Office Space", "Shop", "Showroom"]),
    "ownership": st.selectbox("Ownership", ["Freehold", "Leasehold"]),
    "size_in_sqft": st.number_input("Size in Sqft", value=1200.0),
    "carpet_area_sqft": st.number_input("Carpet Area Sqft", value=1000.0),
    "private_washroom": st.radio("Private Washroom", ["Yes", "No"]),
    "public_washroom": st.radio("Public Washroom", ["Yes", "No"]),
    "floor_no": st.text_input("Floor Number", "5th"),
    "total_floors": st.text_input("Total Floors", "10"),
    "amenities_count": st.number_input("Amenities Count", value=5),
    "electric_charge_included": st.radio("Electric Charge Included", ["Yes", "No"]),
    "water_charge_included": st.radio("Water Charge Included", ["Yes", "No"]),
    "property_age": st.text_input("Property Age", "5-10 years"),
    "possession_status": st.selectbox("Possession Status", ["Immediate", "Under Construction"]),
    "posted_by": st.selectbox("Posted By", ["Owner", "Agent", "Builder"]),
    "rent_increase_per_year": st.text_input("Expected Rent Increase per Year", "5%"),
    "negotiable": st.radio("Is Rent Negotiable?", ["Yes", "No"]),
    "brokerage": st.radio("Brokerage", ["Yes", "No"])
}

if st.button("Predict Rent"):
    try:
        response = requests.post("https://your-fastapi-url.onrender.com/predict", json=input_data)
        if response.status_code == 200:
            st.success(f"🏢 Predicted Monthly Rent: ₹ {response.json()['predicted_rent']}")
        else:
            st.error("❌ Failed to get prediction from server.")
    except Exception as e:
        st.error(f"🔌 Error connecting to API: {e}")
