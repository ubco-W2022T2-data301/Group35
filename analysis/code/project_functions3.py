# Modules required are imported
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

# Load | Process (Load data and add Company column)
def load_and_process(url):
    ls = [["Apple"]*2518,["AMD"]*2518,["Amazon"]*2518, ["Activision"]*2518, ["Ali Baba"]*2030, ["Bank of America"]*2518, ["Salesforce"]*2518,["Cisco"]*2518, ["Disney"]*2518, ["EA"]*2518, ["Ford"]*2518, ["Google"]*2518, ["Intel"]*2518, ["JP Morgan"]*2518, ["CocoCola"]*2518, ["McDonalds"]*2518, ["Meta"]*2518, ["Microsoft"]*2518, ["Match"]*2518, ["Netflix"]*2518, ["Nvidia"]*2518, ["Pfizer"]*2518, ["Paypal"]*1887, ["AT & T"]*2518,["Tesla"]*2518, ["Trade Desk"]*1580, ["Walmart"]*2518, ["Exxon"]*2518, ["Yelp"]*2518, ["Zillow Group"]*2518]  # List for company column
    
    # Chain 1 (Add company names to each row and set index to Company)
    df1 = (
        pd.read_csv(url)
        .assign(Company = [k for i in ls for k in i])
        .set_index('Copmany')
    )

    # Chain 2 (Drop unnecessary columns and process column names)
    df2 = (
        df1.drop(['Open', 'Low', 'Close', ], axis=1)
        .rename(columns={'Adj Close': 'Closed'})
    )

return df2