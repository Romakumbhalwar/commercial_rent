from pydantic import BaseModel
from typing import Literal

class RentRequest(BaseModel):
    city: str
    area: str
    location: str
    zone: str
    location_hub: str
    property_type: str
    ownership: str
    size_in_sqft: float
    carpet_area_sqft: float
    private_washroom: Literal['Yes', 'No']
    public_washroom: Literal['Yes', 'No']
    floor_no: str
    total_floors: str
    amenities_count: int
    electric_charge_included: Literal['Yes', 'No']
    water_charge_included: Literal['Yes', 'No']
    property_age: str
    possession_status: str
    posted_by: str
    rent_increase_per_year: str
    negotiable: Literal['Yes', 'No']
    brokerage: Literal['Yes', 'No']

class RentResponse(BaseModel):
    predicted_rent: float
