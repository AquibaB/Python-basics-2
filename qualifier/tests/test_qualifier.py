# Import pathlib
from pathlib import Path
from qualifier.utils.fileio import save_csv

#Import fileio
from qualifier.utils import fileio

# Import Calculators
from qualifier.utils import calculators

# Import Filters
from qualifier.filters import credit_score
from qualifier.filters import debt_to_income
from qualifier.filters import loan_to_value
from qualifier.filters import max_loan_size

def test_save_csv():
    # Use Path from pathlib to output the test csv to ./data/output/qualifying_loans.csv
    assert Path("/Users/aquiba/Fintech-Workspace/Module_2/bootcamp_challenge2/qualifier/data_qualifying_loans.csv").exists()

def test_calculate_monthly_debt_ratio():
    assert calculators.calculate_monthly_debt_ratio(1500, 4000) == 0.375

def test_calculate_loan_to_value_ratio():
    assert calculators.calculate_loan_to_value_ratio(210000, 250000) == 0.84

def test_filters():
    "Testing loan filters"

    bank_list = fileio.load_csv(Path('./data/daily_rate_sheet.csv'))
    
    current_credit_score = credit_score.filter_credit_score(750, bank_list)
    assert ['Bank of Big - Premier Option', '300000', '0.85', '0.47', '740', '3.6'] in current_credit_score

    dti = debt_to_income.filter_debt_to_income(0.4, bank_list)
    assert ['Bank of Big - Premier Option', '300000', '0.85', '0.47', '740', '3.6'] in dti

    ltv = loan_to_value.filter_loan_to_value(0.6, bank_list)
    assert ['Bank of Big - Premier Option', '300000', '0.85', '0.47', '740', '3.6'] in ltv

    loan_size = max_loan_size.filter_max_loan_size(20000, bank_list)
    assert ['Bank of Big - Premier Option', '300000', '0.85', '0.47', '740', '3.6'] in ltv
