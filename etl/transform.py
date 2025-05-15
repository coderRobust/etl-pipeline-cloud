def clean_data(df):
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
    df.dropna(inplace=True)
    return df
