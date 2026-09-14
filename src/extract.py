import pandas as pd
from src.logger_config import get_logger

logger = get_logger("extract")

# Columns we actually need for this project - trim as you go
USEFUL_COLUMNS = [
    "loan_amnt", "term", "int_rate", "installment", "grade", "sub_grade",
    "emp_length", "home_ownership", "annual_inc", "verification_status",
    "issue_d", "loan_status", "purpose", "dti", "delinq_2yrs",
    "earliest_cr_line", "open_acc", "pub_rec", "revol_bal", "revol_util",
    "total_acc", "addr_state",
]

def extract(filepath: str, chunksize: int = 200_000) -> pd.DataFrame:
    logger.info(f"Extracting data from {filepath} in chunks of {chunksize:,}")

    chunks = []
    total_rows_seen = 0

    for i, chunk in enumerate(
        pd.read_csv(
            filepath,
            usecols=USEFUL_COLUMNS,
            chunksize=chunksize,
            low_memory=False,
        )
    ):
        total_rows_seen += len(chunk)

        # Filter to 2016-2018 while we're already reading chunk by chunk
        chunk["issue_d_parsed"] = pd.to_datetime(chunk["issue_d"], format="%b-%Y", errors="coerce")
        chunk = chunk[chunk["issue_d_parsed"].dt.year.isin([2016, 2017, 2018])]

        if not chunk.empty:
            chunks.append(chunk)

        logger.info(f"Processed chunk {i + 1}: {total_rows_seen:,} rows seen so far")

    df = pd.concat(chunks, ignore_index=True)
    logger.info(f"Extraction complete: {len(df):,} rows kept, {len(df.columns)} columns")
    return df
