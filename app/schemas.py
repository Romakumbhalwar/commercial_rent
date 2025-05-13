from pydantic import BaseModel
import pandas as pd

class CommercialPropertyInput(BaseModel):
    city: str
    area: str
    location: str
    zone: str
    location_hub: str
    property_type: str
    ownership: str
    size_in_sqft: int
    carpet_area_sqft: int
    private_washroom: str
    public_washroom: str
    electric_charge_included: str
    water_charge_included: str
    property_age: str
    possession_status: str
    posted_by: str
    rent_increase_per_year: str
    negotiable: str
    brokerage: str
    floor_no: str
    total_floors: str
    amenities_count: int

    def to_df(self):
        # Convert the schema data to a pandas DataFrame
        data = self.dict()
        df = pd.DataFrame([data])
        return df
