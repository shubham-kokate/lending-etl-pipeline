import pandas as pd
from src.logger_config import get_logger

logger = get_logger("extract")

def extract(filepath: str) -> pd.DataFrame:
    logger.info(f"Extracting data from {filepath}")
    df = pd.read_csv(filepath, low_memory=False)
    logger.info(f"Extracted {len(df):,} rows, {len(df.columns)} columns")
    return df