from pydantic import BaseModel

class CommercialProperty(BaseModel):
    city: str
    area: str
    location: str
    zone: str
    location_hub: str
    property_type: str
    ownership: str
    size_in_sqft: float
    carpet_area_sqft: float
    private_washroom: str
    public_washroom: str
    floor_no: str
    total_floors: str
    amenities_count: int
    electric_charge_included: str
    water_charge_included: str
    property_age: str
    possession_status: str
    posted_by: str
    rent_increase_per_year: str
    negotiable: str
    brokerage: str
