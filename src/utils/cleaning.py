from __future__ import annotations 

import pandas as pd 

class DataCleaner: 
    @staticmethod
    def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
        return df.drop_duplicates().reset_index(drop=True)
    
    @staticmethod
    def enforce_types(df: pd.DataFrame) -> pd.DataFrame:
        """
        Makes sure numeric columns are numeric and categorical columns are strings
        """

        numeric_cols = [
            "Age",
            "Number_of_dependants",
            "Salary",
            "Partner_salary",
            "Total_salary",
            "Price",
        ]

        for col in numeric_cols: 
            df[col] = pd.to_numeric(df[col], errors="coerce")

        categorical_cols = [
             "Gender",
            "Profession",
            "Marital_status",
            "Education",
            "Personal_loan",
            "House_loan",
            "Partner_working",
            "Make",
        ]

        for col in categorical_cols:
            df[col] = df[col].astype("string").str.strip()


        return df 
    

    @staticmethod
    def validate_salary_total(df: pd.DataFrame) -> pd.DataFrame:
        """
        Fix total salary if it does not match Salary + partner_salary
        """

        df = df.copy()

        df['Total_salary'] = df['Salary'] + df['Partner_salary']

        return df 

    @staticmethod
    def clean(df: pd.DataFrame) -> pd.DataFrame:
        """
        Main cleaning pipeline.
        For this dataset, the data is already clean, so the goal is validation
        and standardization rather than heavy mutation.
        """
        df = df.copy()
        df = DataCleaner.enforce_types(df)
        df = DataCleaner.standardize_binary_columns(df)
        df = DataCleaner.validate_salary_total(df)
        df = DataCleaner.remove_duplicates(df)
        return df
    

    

            
    
