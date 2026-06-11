from pathlib import Path
import pandas as pd
from datetime import date

def load_database(path: Path, index: str = None, sheet_name: str =  None) -> pd.DataFrame:
    df = pd.read_excel(path, sheet_name=sheet_name, dtype=str) if sheet_name else pd.read_excel(path, dtype=str)
    df.set_index(index, inplace=True) if index else None
    return df

def parsear_fecha(fecha_str: str, format= "%d-%m-%Y") -> date:
    return date.strptime(fecha_str, format)