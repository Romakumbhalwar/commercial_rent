Commercial Rent Price Prediction

This project uses a machine learning pipeline to predict the rental price of 
commercial properties (like office spaces) based on various property attributes. 
It employs a Random Forest Regressor and includes custom preprocessing logic.

live demo: https://commercial-streamlit.onrender.com

Overview

-  Model: Random Forest Regressor
-  Pipeline: Includes preprocessing (imputation, encoding, scaling) + a custom transformer for Yes/No conversion
-  Input: Commercial property data (`commercial_data.csv`)
-  Output: Trained model (`commercial_rent_model.pkl`)

Features Used

- city, area, location, zone, location_hub
- property_type, ownership, possession_status, posted_by
- size_in_sqft, carpet_area_sqft, floor_no, total_floors
- amenities_count, property_age, rent_increase_per_year, brokerage
- Binary features: private_washroom, public_washroom, electric_charge_included, water_charge_included
- Target: rent_price

Evaluation Metrics

- RMSE: √MSE for measuring prediction error  
- MAE: Mean Absolute Error  
- R² Score: Coefficient of determination 

 

