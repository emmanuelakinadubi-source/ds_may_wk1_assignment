import sys
from pathlib import Path

sys.path.append(str(Path().resolve().parent.parent))

import pandas as pd
from src.utils.cleaning import DataCleaner
from src.utils.data_check import DataCheck


def test_total_salary_validation():
    df = pd.DataFrame({
        "age": [25],
        "gender": ["Male"],
        "profession": ["Salaried"],
        "marital_status": ["Single"],
        "education": ["Graduate"],
        "no_of_dependents": [1],
        "personal_loan": ["Yes"],
        "house_loan": ["No"],
        "partner_working": ["Yes"],
        "salary": [50000],
        "partner_salary": [20000],
        "total_salary": [1],
        "price": [25000],
        "make": ["Hatchback"]
    })

    cleaned = DataCleaner.validate_salary_total(df)
    assert cleaned["total_salary"].iloc[0] == 70000


def test_salary_consistency_detects_no_mismatch():
    df = pd.DataFrame({
        "salary": [50000],
        "partner_salary": [20000],
        "total_salary": [70000]
    })

    mismatch = DataCheck.salary_consistency(df)
    assert mismatch.empty