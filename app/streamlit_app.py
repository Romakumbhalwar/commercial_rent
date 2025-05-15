import streamlit as st
import requests

st.set_page_config(page_title="Commercial Rent Predictor", layout="centered")
st.title("🏢 Commercial Property Rent Prediction")

# ✅ Reset the form: Clear session state and rerun
if st.button("🔄 Reset Data"):
    st.session_state.clear()
    st.rerun()

# ✅ FORM
with st.form("commercial_form"):
    city = st.selectbox("City", ["", "Nagpur"], key="city")
    area = st.text_input("Area", key="area")
    location = st.text_input("Location", key="location")
    location_hub = st.selectbox("Location Hub", ["", "Retail Complex/ Building", "business park", "others", "commercial project", "Market/ High Street", "IT Park"], key="location_hub")
    zone = st.selectbox("Zone", ["", "East", "West", "North", "South"], key="zone")
    property_type = st.selectbox("Property Type", ["", "Office", "Shop", "Showroom", "Warehouse"], key="property_type")
    ownership = st.selectbox("Ownership", ["", "Freehold", "Leasehold", "Rented"], key="ownership")
    size_in_sqft = st.number_input("Size (in sqft)", min_value=0, key="size_in_sqft")
    carpet_area_sqft = st.number_input("Carpet Area (in sqft)", min_value=0, key="carpet_area_sqft")

    private_washroom = st.selectbox("Private Washroom", ["", "Yes", "No"], key="private_washroom")
    public_washroom = st.selectbox("Public Washroom", ["", "Yes", "No"], key="public_washroom")
    electric_charge_included = st.selectbox("Electricity Charges Included", ["", "Yes", "No"], key="electric_charge_included")
    water_charge_included = st.selectbox("Water Charges Included", ["", "Yes", "No"], key="water_charge_included")

    property_age = st.selectbox("Age of Property", ["", "0-1 years", "1-5 years", "5-10 years", "10+ years"], key="property_age")
    possession_status = st.selectbox("Possession Status", ["", "Immediate", "Within 3 Months", "After 3 Months"], key="possession_status")
    posted_by = st.selectbox("Posted By", ["", "Owner", "Agent", "Builder"], key="posted_by")
    rent_increase_per_year = st.selectbox("Yearly Rent Increase", ["", "0%", "5%", "10%", "15%"], key="rent_increase_per_year")
    negotiable = st.selectbox("Rent Negotiable", ["", "Yes", "No"], key="negotiable")
    brokerage = st.selectbox("Brokerage Applicable", ["", "Yes", "No"], key="brokerage")

    floor_no = st.selectbox("Floor Number", ["", "Ground", "1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "9th", "10th", "11th", "12th"], key="floor_no")
    total_floors = st.selectbox("Total Floors in Building", [""] + [str(i) for i in range(1, 13)], key="total_floors")
    amenities_count = st.selectbox("Number of Amenities", [""] + [str(i) for i in range(1, 16)], key="amenities_count")

    submit = st.form_submit_button("Predict Rent")

# ✅ Predict when submitted
if submit:
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
        "electric_charge_included": electric_charge_included,
        "water_charge_included": water_charge_included,
        "property_age": property_age,
        "possession_status": possession_status,
        "posted_by": posted_by,
        "rent_increase_per_year": rent_increase_per_year,
        "negotiable": negotiable,
        "brokerage": brokerage,
        "floor_no": floor_no,
        "total_floors": total_floors,
        "amenities_count": amenities_count,
    }

    with st.spinner("Predicting rent..."):
        try:
            response = requests.post("https://commercial-fastapi.onrender.com/predict", json=input_data)
            result = response.json()
            if "predicted_rent" in result:
                st.success(f"💰 Predicted Monthly Rent: ₹{int(result['predicted_rent']):,}")
            else:
                st.error(f"Error: {result.get('error', 'Unknown error')}")
        except Exception as e:
            st.error(f"🚫 Failed to connect to the prediction API: {e}")
