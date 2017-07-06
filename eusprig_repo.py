import numpy as np

def ebit_to_ebt(ebit: np.array, debt_amount: float, interest_rate: float) -> np.array:
    
    """
    This function calcluations Earnings before Taxes, given an array for EBIT, a debt amount, and an interest rate.
    
    In this example, interest expense is calculated using NumPy's IPMT function, which mirror's that of Excel's.
    
    Parameters
    ==========
    
    ebit : np.array
        array holding annual EBIT figures
        
    debt_amount : float
        the amount of debt used in the np.ipmt function
        
    interest_rate : float
        the interest rate of the debt used to determine interest expense in the np.ipmt function    
    
    Returns
    ===========
    ebt : np.array
        array containing annual EBT figures    
    
    """
    
    periods = len(ebit)
    period_range = np.arange(periods) + 1 
    
    interest_expense = np.ipmt(interest_rate, period_range_yep, periods, -debt_amount)
    
    ebt = ebit - interest_expense
    
    return ebt
    
    
    
    