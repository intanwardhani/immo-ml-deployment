# UTF-8 Python 3.13.5
# Author: Intan K. Wardhani
# Last modified: 03-12-2025


from pydantic import BaseModel, field_validator
from typing import List

class PredictionRequest(BaseModel):
    build_year: float = 2023.0
    build_year_cat: str = "2020s"
    building_state: str = "Good"
    facades: float = 2.0
    garden: int = 1
    living_area: float = 120.0
    locality_name: str = "Namur"
    number_bedrooms: float = 3.0
    postal_code: float = 5000.0
    property_type: str = "Apartment"
    province: str = "Namur"
    swimming_pool: int = 0
    terrace: float = 1.0
    
    # ------------------------
    # Binary field conversion
    # ------------------------
    @field_validator(
        "swimming_pool", 
        "garden", 
        "terrace"
    )
    def yes_no_to_binary(cls, v):
        if isinstance(v, str):
            v = v.strip().lower()
            if v in ["yes", "y", "true", "1"]:
                return 1.0
            if v in ["no", "n", "false", "0"]:
                return 0.0
        return v  # leave unchanged if already 0/1
    
    model_config = {
        "from_attributes": True,    # allows ORM inputs
        "validate_default": True
    }

class BatchPredictionRequest(BaseModel):
    items: List[PredictionRequest]

class PredictionResponse(BaseModel):
    predictions: List[float]
