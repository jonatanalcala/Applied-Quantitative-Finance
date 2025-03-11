# Importing numpy_financial for the necessary financial functions
import numpy_financial as npf

def PV(rate, nper, pmt, fv, when):
    """
    Function to calculate Present Value (PV).

    The Present Value (PV) is the current value of a series of future cash flows,
    given a specific interest rate.

    Parameters:
    rate (float): The interest rate per period.
    nper (int): The number of periods.
    pmt (float): The payment made each period (should be negative if it’s an outgoing payment).
    fv (float): The future value, or a cash balance you want to attain after the last payment is made.
    when (str): The timing of the payment ('begin' for beginning of the period, 'end' for end of the period).

    Returns:
    float: The present value of the series of payments.
    """
    # Calculate Present Value
    return npf.pv(rate, nper, pmt, fv=fv, when=when)


def FV(rate, nper, pmt, pv, when):
    """
    Function to calculate Future Value (FV).

    The Future Value (FV) is the amount of money that you will have at the end of a certain
    number of periods, considering the present value, the rate of return, and periodic payments.

    Parameters:
    rate (float): The interest rate per period.
    nper (int): The number of periods.
    pmt (float): The payment made each period (should be negative if it’s an outgoing payment).
    pv (float): The present value, or the initial investment.
    when (str): The timing of the payment ('begin' for beginning of the period, 'end' for end of the period).

    Returns:
    float: The future value of the investment after the specified number of periods.
    """
    # Calculate Future Value
    return npf.fv(rate, nper, pmt, pv, when=when)


def NPV(rate, values):
    """
    Function to calculate Net Present Value (NPV).

    Net Present Value (NPV) is a method of calculating the present value of all future
    cash flows (positive and negative) of an investment, discounted at a specified rate.

    Parameters:
    rate (float): The discount rate (rate of return).
    values (list of float): A list of cash flows for each period, where the first value is the initial investment.
    
    Returns:
    float: The net present value of the series of cash flows.
    """
    # Calculate Net Present Value
    return npf.npv(rate, values)


def IRR(values):
    """
    Function to calculate Internal Rate of Return (IRR).

    The Internal Rate of Return (IRR) is the discount rate that makes the net present value of
    all future cash flows from a particular project or investment equal to zero.

    Parameters:
    values (list of float): A list of cash flows, where the first value is the initial investment.

    Returns:
    float: The internal rate of return (IRR) for the series of cash flows.
    """
    # Calculate Internal Rate of Return
    return npf.irr(values)

