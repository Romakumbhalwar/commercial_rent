from pydantic import BaseModel

class CommercialPropertyFeatures(BaseModel):
    area: float
    location: str
    size: float
    property_type: str
    furnishing: str
    security: float
    maintenance: float
    brokerage: float
    amenities: int
    age: int
    floor: int
    total_floor: int
    carpet_area: float
    lease_type: str
    gated_security: str  # 'Yes' or 'No'
