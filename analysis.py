
import pandas as pd

def calculate_stats(df, column):
    return {
        "mean": df[column].mean(),
        "median": df[column].median(),
        "std_dev": df[column].std(),
        "25_percentile": df[column].quantile(0.25),
        "75_percentile": df[column].quantile(0.75),
    }

def group_by_summary(df, group_col, value_col):
    return df.groupby(group_col)[value_col].mean()
