
import pandas as pd

def moving_average(df, column, window=3):
    return df[column].rolling(window=window).mean()

def growth_rate(df, column):
    return df[column].pct_change() * 100

def trend_analysis(df, column):
    return {
        "moving_average": moving_average(df, column),
        "growth_rate": growth_rate(df, column)
    }
