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


def backward_steps_for_client(steps , client, variation)->dict:
    count_backward=0
    for i in range (1, len(steps)):
         if (steps[i-1] - steps[i] != 1):
             count_backward=count_backward+1
    total_steps=len(steps)-1
    return {client:count_backward/total_steps if total_steps > 0 else 0}