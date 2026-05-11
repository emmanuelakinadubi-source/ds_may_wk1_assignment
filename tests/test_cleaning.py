import sys
from pathlib import Path

sys.path.append(str(Path().resolve().parent.parent))

import pandas as pd
from src.utils.cleaning import DataCleaner
from src.utils.data_check import DataCheck


def test_total_salary_validation():
    df = pd.DataFrame({
        "Age": [25],
        "Gender": ["Male"],
        "Profession": ["Salaried"],
        "Marital_status": ["Single"],
        "Education": ["Graduate"],
        "No_of_Dependents": [1],
        "Personal_loan": ["Yes"],
        "House_loan": ["No"],
        "Partner_working": ["Yes"],
        "Salary": [50000],
        "Partner_salary": [20000],
        "Total_salary": [1],
        "Price": [25000],
        "Make": ["Hatchback"]
    })

    cleaned = DataCleaner.validate_salary_total(df)
    assert cleaned["Total_salary"].iloc[0] == 70000


def test_salary_consistency_detects_no_mismatch():
    df = pd.DataFrame({
        "Salary": [50000],
        "Partner_salary": [20000],
        "Total_salary": [70000]
    })
    mismatch = DataCheck.salary_consistency(df)
    assert mismatch.empty