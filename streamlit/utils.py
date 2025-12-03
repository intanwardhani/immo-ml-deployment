# UTF-8 Python 3.13.5
# Author: Intan K. Wardhani
# Last modified: 02-12-2025


def yes_no_to_binary(v):
    """
    Convert Yes/No from Streamlit UI to 1/0
    (Optional, API already handles this via validators)
    """
    
    if isinstance(v, str):
        v = v.strip().lower()
        if v in ["yes", "y", "true", "1"]:
            return 1.0
        if v in ["no", "n", "false", "0"]:
            return 0.0
    return v  # leave unchanged if already 0/1