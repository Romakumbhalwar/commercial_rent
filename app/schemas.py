from pydantic import BaseModel

class CommercialProperty(BaseModel):
    city: str
    area: str
    location: str
    zone: str
    property_type: str
    ownership: str
    size_in_sqft: float
    carpet_area_sqft: float
    private_washroom: str  # "Yes" or "No"
    public_washroom: str   # "Yes" or "No"
    floor_no: str
    total_floors: str
    amenities_count: int
    electric_charge_included: str  # "Yes" or "No"
    water_charge_included: str     # "Yes" or "No"
    possession_status: str
