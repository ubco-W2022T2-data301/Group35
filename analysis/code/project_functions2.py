## Load and Processing Functions
import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt

def load_and_process(url):
    # Makes the list for the company columns
    list = [["Apple"]*2518, ["AMD"]*2518, ["Amazon"]*2518, ["Activision"]*2518, ["Alibaba"]*2030,["Bank of America"]*2518, ["Salesforce"]*2518, ["Cisco"]*2518, ["Disney"]*2518, ["EA"]*2518,  ["Ford"]*2518, ["Google"]*2518, ["Intel"]*2518, ["JP Morgan"]*2518, ["CocoCola"]*2518, ["McDonalds"]*2518, ["Meta"]*2518, ["Microsoft"]*2518, ["Match"]*2518, ["Netflix"]*2518, ["Nvidia"]*2518, ["Pfizer"]*2518, ["Paypal"]*1887, ["AT & T"]*2518, ["Tesla"]*2518, ["Trade Desk"]*1580, ["Walmart"]*2518, ["Exxon"]*2518, ["Yelp"]*2518, ["Zillow Group"]*2518]
    # the first method chain makes Company as the index
    df1 = (   
        pd.read_csv(url)
        .assign(Company = [k for i in list for k in i])  # this makes a company column
        .set_index("Company")
    )

    # the second method chain drops the unecessary columns and selects the needed columns and processes them
    df2 = (
        df1.drop(['Close', 'Date'], axis = 1)
        .loc[:,['Profit']]
    )

    return df2 # we ensure that we return the updated and new data frame