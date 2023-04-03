## LOAD AND PROCESS FUNCTION

import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt

def load_and_process(url):
    # Define list for company column
    list = [["Apple"]*2518, ["AMD"]*2518, ["Amazon"]*2518, ["Activision"]*2518, ["Alibaba"]*2030, 
            ["Bank of America"]*2518, ["Salesforce"]*2518, ["Cisco"]*2518, ["Disney"]*2518, ["EA"]*2518, 
            ["Ford"]*2518, ["Google"]*2518, ["Intel"]*2518, ["JP Morgan"]*2518, ["CocoCola"]*2518, 
            ["McDonalds"]*2518, ["Meta"]*2518, ["Microsoft"]*2518, ["Match"]*2518, ["Netflix"]*2518, 
            ["Nvidia"]*2518, ["Pfizer"]*2518, ["Paypal"]*1887, ["AT & T"]*2518, ["Tesla"]*2518, 
            ["Trade Desk"]*1580, ["Walmart"]*2518, ["Exxon"]*2518, ["Yelp"]*2518, ["Zillow Group"]*2518]
  
    # Define dictionary for industries
    industries = {"Apple": "Technology", "AMD": "Technology" , "Amazon": "Retail", "Activision": "Gaming", 
                  "Alibaba": "Retail", "Bank of America": "Finance", "Salesforce": "Technology", "Cisco": "Technology", 
                  "Disney": "Entertainment", "EA": "Gaming", "Ford": "Automotive", "Google": "Technology", 
                  "Intel": "Technology", "JP Morgan": "Finance", "CocoCola": "Beverage", "McDonalds": "Fast Food", 
                  "Meta": "Technology", "Microsoft": "Technology", "Match": "Online Dating", "Netflix": "Entertainment", 
                  "Nvidia": "Technology", "Pfizer": "Pharmaceuticals", "Paypal": "Finance", "AT & T": "Telecommunications", 
                  "Tesla": "Automotive", "Trade Desk": "Advertising", "Walmart": "Retail", "Exxon": "Oil and Gas", 
                  "Yelp": "Technology", "Zillow Group": "Real Estate"}
    
    # Method Chain 1 (Load data and deal with missing data)
    df1 = (
        pd.read_csv(url)
        # Make a new column for company
        .assign(Company = [k for i in list for k in i])
        .assign(Industry = lambda x: x['Company'].map(industries))
        # Add a new column for industry since i will be looking at these stocks within the indusrties as well
        #df = df[['Company', 'Industry', 'Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']]
    )  

    # Method Chain 2 (Create new columns, drop others, and do processing)
    df2 = (
        df1.assign(Profit_Made=df1['Close']-df1['Open'])
        .loc[df1['Industry'] == 'Technology'].groupby('Company')['Profit_Made'].mean()
    )

    # Make sure to return the latest dataframe
    return df2 
