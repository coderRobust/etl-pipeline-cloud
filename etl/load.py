import pandas as pd
import sqlalchemy
from config.settings import DATABASE_URL


def load_to_db(df: pd.DataFrame, table_name: str):
    engine = sqlalchemy.create_engine(DATABASE_URL)
    df.to_sql(table_name, engine, if_exists="replace", index=False)
    print(f" Loaded {len(df)} rows to '{table_name}' table")
