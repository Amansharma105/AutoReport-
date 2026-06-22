
import pandas as pd

def z_score_outliers(df, column):
    mean = df[column].mean()
    std = df[column].std()

    z_scores = (df[column] - mean) / std

    return df[abs(z_scores) > 2]


def iqr_outliers(df, column):
    q1 = df[column].quantile(0.25)
    q3 = df[column].quantile(0.75)

    iqr = q3 - q1

    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr

    return df[(df[column] < lower) | (df[column] > upper)]
