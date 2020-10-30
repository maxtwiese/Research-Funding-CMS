import pandas as pd
import numpy as np
from scipy import stats


def cleaning(path):

    """
    Creates a dataframe from Open Payments CMS data that is focused
    on research related to a product or products. Built to work with:
        Research Payment Data – Detailed Dataset 2016 Reporting Year
        Research Payment Data – Detailed Dataset 2017 Reporting Year
        Research Payment Data – Detailed Dataset 2018 Reporting Year
        Research Payment Data – Detailed Dataset 2019 Reporting Year
    Field names are different for reporting years 2015 and earlier,
    but only requires minor adjustment. Data was downloaded from
    https://openpaymentsdata.cms.gov/browse?limitTo=datasets and
    should be downloaded as a CSV file to recreate my exploration.

    Parameters
    ----------
    path : string
        the file path to where you saved the CSV

    Returns
    -------
    df : DataFrame
        dataframe with # entries for # financial relateionships and 7
        fields.
    """

    # Read in CSV
    df = pd.read_csv(
        path,
        low_memory=False,
        usecols=[
            'Related_Product_Indicator', 'Covered_Recipient_Type',
            'Recipient_State','Total_Amount_of_Payment_USDollars',
            'Indicate_Drug_or_Biological_or_Device_or_Medical_Supply_1',
            'Indicate_Drug_or_Biological_or_Device_or_Medical_Supply_2',
            'Indicate_Drug_or_Biological_or_Device_or_Medical_Supply_3',
            'Indicate_Drug_or_Biological_or_Device_or_Medical_Supply_4',
            'Indicate_Drug_or_Biological_or_Device_or_Medical_Supply_5'])

    # Create field True for enrtries related to at least one Drug
    df.loc[
        (df[
            'Indicate_Drug_or_Biological_or_Device_or_Medical_Supply_1'
            ] == 'Drug')
        | (df[
            'Indicate_Drug_or_Biological_or_Device_or_Medical_Supply_2'
            ] == 'Drug')
        | (df[
            'Indicate_Drug_or_Biological_or_Device_or_Medical_Supply_3'
            ] == 'Drug')
        | (df[
            'Indicate_Drug_or_Biological_or_Device_or_Medical_Supply_4'
            ] == 'Drug')
        | (df[
            'Indicate_Drug_or_Biological_or_Device_or_Medical_Supply_5'
            ] == 'Drug'),
        'Drug_Related'
    ] = True

    df.loc[
        (df[
            'Indicate_Drug_or_Biological_or_Device_or_Medical_Supply_1'
            ] != 'Drug')
        & (df[
            'Indicate_Drug_or_Biological_or_Device_or_Medical_Supply_2'
            ] != 'Drug')
        & (df[
            'Indicate_Drug_or_Biological_or_Device_or_Medical_Supply_3'
            ]!= 'Drug')
        & (df[
            'Indicate_Drug_or_Biological_or_Device_or_Medical_Supply_4'
            ] != 'Drug')
        & (df[
            'Indicate_Drug_or_Biological_or_Device_or_Medical_Supply_5'
            ] != 'Drug'),
        'Drug_Related'
    ] = False

    # Create field True for enrtries related to at least one Biological
    df.loc[
        (df[
            'Indicate_Drug_or_Biological_or_Device_or_Medical_Supply_1'
            ] == 'Biological')
        | (df[
            'Indicate_Drug_or_Biological_or_Device_or_Medical_Supply_2'
            ] == 'Biological')
        | (df[
            'Indicate_Drug_or_Biological_or_Device_or_Medical_Supply_3'
            ] == 'Biological')
        | (df[
            'Indicate_Drug_or_Biological_or_Device_or_Medical_Supply_4'
            ] == 'Biological')
        | (df[
            'Indicate_Drug_or_Biological_or_Device_or_Medical_Supply_5'
            ] == 'Biological'),
        'Biological_Related'
    ] = True

    df.loc[
        (df[
            'Indicate_Drug_or_Biological_or_Device_or_Medical_Supply_1'
            ] != 'Biological')
        & (df[
            'Indicate_Drug_or_Biological_or_Device_or_Medical_Supply_2'
            ] != 'Biological')
        & (df[
            'Indicate_Drug_or_Biological_or_Device_or_Medical_Supply_3'
            ] != 'Biological')
        & (df[
            'Indicate_Drug_or_Biological_or_Device_or_Medical_Supply_4'
            ] != 'Biological')
        & (df[
            'Indicate_Drug_or_Biological_or_Device_or_Medical_Supply_5'
            ] != 'Biological'),
        'Biological_Related'
    ] = False

    # Create field True for enrtries related to at least one Device
    df.loc[
        (df[
            'Indicate_Drug_or_Biological_or_Device_or_Medical_Supply_1'
            ] == 'Device')
        | (df[
            'Indicate_Drug_or_Biological_or_Device_or_Medical_Supply_2'
            ] == 'Device')
        | (df[
            'Indicate_Drug_or_Biological_or_Device_or_Medical_Supply_3'
            ] == 'Device')
        | (df[
            'Indicate_Drug_or_Biological_or_Device_or_Medical_Supply_4'
            ] == 'Device')
        | (df[
            'Indicate_Drug_or_Biological_or_Device_or_Medical_Supply_5'
            ] == 'Device'),
        'Device_Related'
    ] = True

    df.loc[
        (df[
            'Indicate_Drug_or_Biological_or_Device_or_Medical_Supply_1'
            ] != 'Device')
        & (df[
            'Indicate_Drug_or_Biological_or_Device_or_Medical_Supply_2'
            ] != 'Device')
        & (df[
            'Indicate_Drug_or_Biological_or_Device_or_Medical_Supply_3'
            ] != 'Device')
        & (df[
            'Indicate_Drug_or_Biological_or_Device_or_Medical_Supply_4'
            ] != 'Device')
        & (df[
            'Indicate_Drug_or_Biological_or_Device_or_Medical_Supply_5'
            ] != 'Device'),
        'Device_Related'
    ] = False

    # Drop uneeded fields
    df = df.drop(
        columns = [
            'Indicate_Drug_or_Biological_or_Device_or_Medical_Supply_1',
            'Indicate_Drug_or_Biological_or_Device_or_Medical_Supply_2',
            'Indicate_Drug_or_Biological_or_Device_or_Medical_Supply_3',
            'Indicate_Drug_or_Biological_or_Device_or_Medical_Supply_4',
            'Indicate_Drug_or_Biological_or_Device_or_Medical_Supply_5',
        ]
    )
    return df


def stats_of_interest(arr1, arr2):

    """
    Calculates statistics of interest for two array like objest
    should be downloaded as a CSV file to recreate my exploration.

    Parameters
    ----------
    arr1, arr2 : array like

    Returns
    -------
    var1, va2 : float64
        variance
    tscore : float 64
        ttest statistic for arr1 & arr2
    pval : float64
        p-value for ar1 & arr2
    """

    var1 = np.var(arr1)
    var2 = np.var(arr2)
    tscore, pval = stats.ttest_ind(arr1, arr2)
    return var1, var2, tscore, pval

