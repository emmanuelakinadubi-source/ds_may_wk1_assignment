from __future__ import annotations

import pandas as pd


class InsightService:
    @staticmethod
    def make_share(df: pd.DataFrame) -> pd.Series:
        return (df["Make"].value_counts(normalize=True) * 100).round(1)

    @staticmethod
    def make_summary(df: pd.DataFrame) -> pd.DataFrame:
        return df.groupby("Make").agg(
            count=("Make", "size"),
            avg_age=("Age", "mean"),
            avg_salary=("Salary", "mean"),
            avg_partner_salary=("Partner_salary", "mean"),
            avg_total_salary=("Total_salary", "mean"),
            avg_price=("Price", "mean"),
            avg_dependents=("No_of_Dependents", "mean"),
        ).round(2)

    @staticmethod
    def business_insights(df: pd.DataFrame) -> list[str]:
        make_share = (df["Make"].value_counts(normalize=True) * 100).round(1)
        make_summary = df.groupby("Make").agg(
            avg_age=("Age", "mean"),
            avg_total_salary=("Total_salary", "mean"),
            avg_price=("Price", "mean"),
        ).round(2)

        insights = []

        top_make = make_share.idxmax()
        insights.append(
            f"{top_make} is the most preferred car type in the dataset "
            f"({make_share.max()}% of customers), so it is the strongest mass-market segment."
        )

        oldest_make = make_summary["avg_age"].idxmax()
        insights.append(
            f"{oldest_make} buyers are the oldest on average "
            f"({make_summary['avg_age'].max():.1f} years), suggesting life-stage affects purchase choice."
        )

        richest_make = make_summary["avg_total_salary"].idxmax()
        insights.append(
            f"{richest_make} buyers have the highest average household income "
            f"({make_summary['avg_total_salary'].max():,.0f}), which supports premium positioning."
        )

        expensive_make = make_summary["avg_price"].idxmax()
        insights.append(
            f"{expensive_make} has the highest average price "
            f"({make_summary['avg_price'].max():,.0f}), so it should be targeted to higher-income segments."
        )

        house_loan_table = pd.crosstab(df["House_loan"], df["Make"])
        if "SUV" in house_loan_table.columns and house_loan_table.loc["Yes", "SUV"] == 0:
            insights.append(
                "Customers with a house loan did not purchase SUVs in this dataset, "
                "which suggests debt burden is linked to lower vehicle choice."
            )

        return insights