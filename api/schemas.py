# UTF-8 Python 3.13.5
# Author: Intan K. Wardhani
# Last modified: 03-12-2025


from pydantic import BaseModel, field_validator
from typing import List

class PredictionRequest(BaseModel):
    build_year: float
    build_year_cat: str
    building_state: str
    facades: float
    garden: int
    living_area: float
    locality_name: str
    number_bedrooms: float
    postal_code: float
    property_type: str
    province: str
    swimming_pool: int
    terrace: float
    
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
