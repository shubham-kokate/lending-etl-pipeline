from src.extract import extract
from src.clean import clean
from src.logger_config import get_logger

logger = get_logger("pipeline")

# RAW_FILE = "raw_data/accepted_2007_to_2018Q4.csv"
RAW_FILE = 'raw_data/accepted_2007_to_2018Q4.csv'

USEFUL_COLUMNS = [
    "loan_amnt", "term", "int_rate", "installment", "grade", "sub_grade",
    "emp_length", "home_ownership", "annual_inc", "verification_status",
    "issue_d", "loan_status", "purpose", "dti", "delinq_2yrs",
    "earliest_cr_line", "open_acc", "pub_rec", "revol_bal", "revol_util",
    "total_acc", "addr_state", "issue_d_parsed"
]

def main():
    logger.info("=== Pipeline run started ===")
    df = extract(RAW_FILE)

    """
    EXPLORATION CODE
    """

    print(df.info())
    print('*'*150)

    print(df.isnull().sum().sort_values(ascending=False))
    print('*'*150)

    print((df.isnull().sum() / len(df) * 100).sort_values(ascending=False))
    print('*'*150)

    for col in USEFUL_COLUMNS:
        print(f"\n--- {col} ---")
        print("dtype:", df[col].dtype)
        print("nulls:", df[col].isnull().sum())
        print("unique values:", df[col].nunique())
        print(df[col].unique()[:15])
        
    

    """
    EXPLORATION CODE
    """
    # TODO: clean(df)
    df = clean(df)    
    
    
    # TODO: transform(df)
    # TODO: validate(df)
    # TODO: load(df)

    logger.info("=== Pipeline run complete ===")

if __name__ == "__main__":
    main()