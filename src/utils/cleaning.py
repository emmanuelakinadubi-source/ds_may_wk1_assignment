from __future__ import annotations

import pandas as pd


class DataCleaner:

    @staticmethod
    def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
        return df.drop_duplicates().reset_index(drop=True)

    @staticmethod
    def enforce_types(df: pd.DataFrame) -> pd.DataFrame:
        """
        Ensure numeric columns are numeric and categorical columns are strings.
        """

        numeric_cols = [
            "age",
            "no_of_dependents",
            "salary",
            "partner_salary",
            "total_salary",
            "price",
        ]

        for col in numeric_cols:
            df[col] = pd.to_numeric(df[col], errors="coerce")

        categorical_cols = [
            "gender",
            "profession",
            "marital_status",
            "education",
            "personal_loan",
            "house_loan",
            "partner_working",
            "make",
        ]

        for col in categorical_cols:
            df[col] = df[col].astype("string").str.strip()

        return df

    @staticmethod
    def validate_salary_total(df: pd.DataFrame) -> pd.DataFrame:
        """
        Fix total_salary if it does not match salary + partner_salary.
        """

        df = df.copy()

        df["total_salary"] = (
            df["salary"] + df["partner_salary"]
        )

        return df

    @staticmethod
    def standardize_binary_columns(df: pd.DataFrame) -> pd.DataFrame:
        """
        Standardize Yes/No fields to title case.
        """

        binary_cols = [
            "personal_loan",
            "house_loan",
            "partner_working"
        ]

        for col in binary_cols:
            df[col] = (
                df[col]
                .str.strip()
                .str.title()
            )

        return df

    @staticmethod
    def clean(df: pd.DataFrame) -> pd.DataFrame:
        """
        Main cleaning pipeline.

        Steps:
        1. Create dataframe copy
        2. Standardize column names
        3. Enforce correct data types
        4. Standardize binary/categorical values
        5. Validate salary calculations
        6. Remove duplicates
        """

        df = df.copy()

        # Standardize column names
        df.columns = (
            df.columns
            .str.strip()
            .str.lower()
        )

        # Apply cleaning steps
        df = DataCleaner.enforce_types(df)
        df = DataCleaner.standardize_binary_columns(df)
        df = DataCleaner.validate_salary_total(df)
        df = DataCleaner.remove_duplicates(df)

        return df