from extract import extract_csv
from transform import clean_data
from load import load_to_db

if __name__ == "__main__":
    df = extract_csv("data/sales_data.csv")
    df_clean = clean_data(df)
    load_to_db(df_clean, "sales_data")
