from pydantic import BaseModel
from typing import Optional

class RentInput(BaseModel):
    city: str
    area: str
    location: str
    zone: str
    location_hub: str
    property_type: str
    ownership: str
    size_in_sqft: float
    carpet_area_sqft: float
    private_washroom: str  # Expecting "Yes" or "No"
    public_washroom: str   # Expecting "Yes" or "No"
    floor_no: str
    total_floors: str
    amenities_count: int
    electric_charge_included: str  # "Yes"/"No"
    water_charge_included: str     # "Yes"/"No"
    property_age: str
    possession_status: str
    posted_by: str
    rent_increase_per_year: str
    negotiable: str
    brokerage: str
