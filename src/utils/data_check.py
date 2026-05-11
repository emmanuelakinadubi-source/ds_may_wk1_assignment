from __future__ import annotations 

import numpy as np 
import pandas as pd 


class DataCheck:
    @staticmethod
    def overview(df: pd.DataFrame) ->dict: 
        """This will return a compact overview """
        return {
            "shape":df.shape,
            "missing_values": df.isna().sum(),
            "missing_percentage": (df.isna().mean() * 100).round(2),
            "duplicate_rows": int(df.duplicated().sum()),
            "dtypes": df.dtypes
        }
    
    @staticmethod
    def summary_stat(df: pd.DataFrame) -> pd.DataFrame:
        """ Summary Stats for numerical and categorical columns"""
        return df.describe(include="all").T
    
    @staticmethod
    def unique_values(df: pd.DataFrame) -> pd.Series:
        """This will check number of unique values per each column"""
        return df.nunique()
    
    @staticmethod
    def salary_consistency(df: pd.DataFrame) -> pd.DataFrame:

        expected = (
            df["salary"] +
            df["partner_salary"]
        )

        mismatch = df.loc[
            ~expected.eq(df["total_salary"])
        ].copy()

        mismatch["expected_total_salary"] = expected.loc[mismatch.index]

        return mismatch
    
    @staticmethod
    def iqr_outlier_report(df: pd.DataFrame, column:str) ->dict:
        """Returns IQR outlier info for a numeric value!"""

        q1 = df[column].quantile(0.25)
        q3 = df[column].quantile(0.75)
        iqr = q3 - q1 
        lower = q1 - 1.5 * iqr 
        upper = q3 + 1.5 * iqr 
        outliers = df[(df[column] < lower | df[column] > upper)]
        return {
            "column": column,
            "lower_bound": lower, 
            "upper_bound": upper, 
            "outlier_count": len(outliers),
            "outlier_rows": outliers
        }
    
    def category_count(df: pd.DataFrame, column:str) -> pd.Series:
        """This is frequency tabe for categorical column"""

        return df[column].value_counts(dropna=False)


    

