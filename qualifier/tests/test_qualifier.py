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
    '''Test saving qulifying loans to CSV file'''

    assert Path("/Users/aquiba/Fintech-Workspace/Module_2/bootcamp_challenge2/qualifier/data_qualifying_loans.csv").exists()

def test_calculate_monthly_debt_ratio():
    '''Test the monthly debt ratio calculation
    
    Args:
        Debt outstanding
        Income

    Test:
        Debt / income
    '''

    assert calculators.calculate_monthly_debt_ratio(1500, 4000) == 0.375

def test_calculate_loan_to_value_ratio():
    '''Test the monthly debt ratio calculation
    
    Args: 
        Loan requested
        Home value

    Test:
        Loan / home value 
    '''
    assert calculators.calculate_loan_to_value_ratio(210000, 250000) == 0.84

def test_filters():
    '''Test of loan filters
    
    Arg:
        Credit score
        Debt to income
        Loan to value
        Max loan size
        Bank list
    
    Tests:
        Loan meets credit score filter
        Loan meets debt to income filter
        Loan meets loan to value filter
        Loan meets max loan size filter
    
    '''

    bank_list = fileio.load_csv(Path('./data/daily_rate_sheet.csv'))

    current_credit_score = credit_score.filter_credit_score(750, bank_list)
    assert ['Bank of Big - Premier Option', '300000', '0.85', '0.47', '740', '3.6'] in current_credit_score

    dti = debt_to_income.filter_debt_to_income(0.4, bank_list)
    assert ['Bank of Big - Premier Option', '300000', '0.85', '0.47', '740', '3.6'] in dti

    ltv = loan_to_value.filter_loan_to_value(0.6, bank_list)
    assert ['Bank of Big - Premier Option', '300000', '0.85', '0.47', '740', '3.6'] in ltv

    loan_size = max_loan_size.filter_max_loan_size(20000, bank_list)
    assert ['Bank of Big - Premier Option', '300000', '0.85', '0.47', '740', '3.6'] in ltv
