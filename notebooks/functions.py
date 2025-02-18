import pandas as pd
import scipy.stats as st
import numpy as np

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


def two_proportion_test(x1, n1, x2, n2, alpha=0.10):
    """
    Perform two-proportion z-test
    
    Parameters:
    x1: successes in first group (Test)
    n1: total sample size of first group
    x2: successes in second group (Control)
    n2: total sample size of second group
    alpha: significance level (default 0.05)
    
    Returns:
    Dictionary with test results
    """
    # Calculate sample proportions
    p1 = x1/n1
    p2 = x2/n2
    
    # Calculate pooled sample proportion
    p_pooled = (x1 + x2)/(n1 + n2)
    q_pooled = 1 - p_pooled
    
    # Check assumptions
    assumptions_met = all([
        n1 * p1 >= 5, n1 * (1-p1) >= 5,
        n2 * p2 >= 5, n2 * (1-p2) >= 5
    ])
    
    # Calculate test statistic
    z = (p1 - p2) / np.sqrt(p_pooled * q_pooled * (1/n1 + 1/n2))
    
    # Calculate p-value (two-tailed test)
    p_value = 2 * (1 - st.norm.cdf(abs(z)))
    
    return {
        'p1': p1,
        'p2': p2,
        'z_statistic': z,
        'p_value': p_value,
        'significant': p_value < alpha,
        'assumptions_met': assumptions_met
    }

def backward_steps_for_client(steps , client, variation)->dict:
    count_backward=0
    for i in range (1, len(steps)):
         if (steps[i-1] - steps[i] != 1):
             count_backward=count_backward+1
    total_steps=len(steps)-1
    return {client:count_backward/total_steps if total_steps > 0 else 0}

