# UTF-8 Python 3.13.5
# Author: Intan K. Wardhani
# Last modified: 02-12-2025


import numpy as np
import pandas as pd
import joblib

def predict(data, pipeline=None, model_path=None):
    """
    Predict house prices using a loaded pipeline.

    Parameters
    ----------
    data : dict | pd.DataFrame
        Input sample or batch.
    pipeline : Pipeline, optional
        Already-loaded model pipeline.
    model_path : str, optional
        Path to model if pipeline not provided.

    Returns
    -------
    np.ndarray
        Array of predicted prices in original price scale.
    """

    if pipeline is None and model_path is None:
        raise ValueError("Either `pipeline` or `model_path` must be provided.")

    if pipeline is None:
        pipeline = joblib.load(model_path)

    # Convert input to DataFrame
    if isinstance(data, dict):
        df = pd.DataFrame([data])
    else:
        df = pd.DataFrame(data)

    # Convert yes/no strings to binary (optional safety)
    binary_cols = ["swimming_pool", "garden", "terrace"]
    for col in binary_cols:
        if col in df.columns:
            df[col] = df[col].apply(lambda x: 1 if str(x).strip().lower() in ["yes","y","true","1"] else 0 if str(x).strip().lower() in ["no","n","false","0"] else x)

    preds = pipeline.predict(df)

    # Inverse log-transform if Ridge
    if hasattr(pipeline.named_steps["regressor"], "alpha"):
        preds = np.expm1(preds)

    return preds

if __name__ == "__main__":
    sample = {
        "living_area": 120.0,
        "postal_code": 9000,
        "number_bedrooms": 3,
        "build_year": 2019,
        "build_year_cat": "2010s",
        "building_state": "New",
        "locality_name": "Gent",
        "property_type": "House",
        "province": "East Flanders",
        "swimming_pool": "no",
        "garden": "yes",
        "terrace": "yes",
        "facades": 2
    }

    print("Prediction:", predict(sample))
  

    

