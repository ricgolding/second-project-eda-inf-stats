import pandas as pd

def save_to_csv(df: pd.DataFrame, csv_name: str):
    """
    Save a DataFrame to a CSV file in the '../data/clean/' directory.

    Parameters:
    df (pd.DataFrame): The DataFrame to be saved.
    csv_name (str): The name of the CSV file (without path) to save the DataFrame.

    Returns:
    None
    """
    directory_path = '../data/clean/'
    full_path = directory_path + csv_name
    df.to_csv(full_path, index=False)
    print(f"DataFrame successfully saved to {full_path}")