from src.extract import extract
from src.logger_config import get_logger

logger = get_logger("pipeline")

# RAW_FILE = "raw_data/accepted_2007_to_2018Q4.csv"
RAW_FILE = 'raw_data/accepted_2007_to_2018Q4.csv'

def main():
    logger.info("=== Pipeline run started ===")
    df = extract(RAW_FILE)

    # TODO: filter to 2016-2018 via issue_d
    # TODO: clean(df)
    # TODO: transform(df)
    # TODO: validate(df)
    # TODO: load(df)

    logger.info("=== Pipeline run complete ===")

if __name__ == "__main__":
    main()