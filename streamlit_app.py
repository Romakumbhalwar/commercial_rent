import streamlit as st
import requests

st.title("Commercial Rent Price Prediction")
st.markdown("Enter commercial property details to get rent prediction:")

form = st.form("rent_form")
city = form.text_input("City")
area = form.text_input("Area")
location = form.text_input("Location")
zone = form.text_input("Zone")
location_hub = form.text_input("Location Hub")
property_type = form.selectbox("Property Type", ["Office", "Shop", "Warehouse","showroom","bere shell"])
ownership = form.selectbox("Ownership", ["Freehold", "Leasehold"])
size_in_sqft = form.number_input("Size in Sqft", min_value=0.0)
carpet_area_sqft = form.number_input("Carpet Area in Sqft", min_value=0.0)
private_washroom = form.selectbox("Private Washroom", ["Yes", "No"])
public_washroom = form.selectbox("Public Washroom", ["Yes", "No"])
floor_no = form.text_input("Floor Number (e.g., 5th)")
total_floors = form.text_input("Total Floors")
amenities_count = form.slider("Amenities Count", 0, 20)
electric_charge_included = form.selectbox("Electric Charge Included", ["Yes", "No"])
water_charge_included = form.selectbox("Water Charge Included", ["Yes", "No"])
property_age = form.text_input("Property Age (e.g., 5-10 years)")
possession_status = form.selectbox("Possession Status", ["ready to move", "Within 3 Months", "After 3 Months","under construction"])
posted_by = form.selectbox("Posted By", ["Owner", "Agent"])
rent_increase_per_year = form.text_input("Rent Increase Per Year (e.g., 5%)")
negotiable = form.selectbox("Negotiable", ["Yes", "No"])
brokerage = form.selectbox("Brokerage", ["Yes", "No"])

submit = form.form_submit_button("Predict Rent")

if submit:
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
        response = requests.post("https://rental-price-api.onrender.com/predict", json=payload)
        st.write("Response status code:", response.status_code)
        if response.status_code == 200:
            predicted = response.json()['predicted_rent']
            st.success(f"Predicted Rent: ₹ {predicted}/month")
        else:
            st.error(f"❌ Server error: {response.status_code}")
            st.error(f"Details: {response.text}")
    except Exception as e:
        st.error("❌ Request failed")
        st.error(str(e))