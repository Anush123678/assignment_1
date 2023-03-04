#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 21:34:51 2023

@author: anush
"""

import pandas as pd
import matplotlib.pyplot as plt


def products_distribution(data, products, title):
    """

    Parameters
    ----------
    data : Panda's DataFrame Object
        data parameter is used to provide product brands and count of these
        products. Each value contains brand name and its product's count at 
        Amazon platform.
    products : Array
        It contains the brands of concern. 

    Returns
    -------
    None.

    """
    data_copy = data.copy()
    per = (data_copy / data_copy.sum()) * 100
    per["Others"] = per.sum() - (per.loc[products].sum())
    products_copy = products.copy()
    products_copy.append("Others")
    plt.pie(per.loc[products_copy], labels=per.loc[products_copy].index, 
            autopct='%1.1f%%', startangle=90)
    plt.title(title)
    plt.axis('equal')
    
    plt.show()
    

def bar_plot_products_count(data, title, x_label, y_label):
    """
    Parameters
    ----------
    data : DataFrame
        Data to display in distribution.
    title : String
        Title to be shown on the top of graph.
    x_label : String
        x-axis label.
    y_label : String
        y-axis label.

    Returns
    -------
    None.

    """
    ax = data.plot(kind='bar', figsize=(10, 6), width=0.8)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_title(title)
    ax.legend()
    plt.show()
    

def line_graph(data, title):
    """
    Parameters
    ----------
    data : DataFrame
        Holding data to display line chart for BitCoin.
    title: String
        Title of the graph
    Returns
    -------
    None.
    """
    data = data.iloc[::-1] # To reverse the data
    plt.plot(data['Date'], data['Open'])
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel("Price in Open Market ($)")
    plt.xticks(rotation = 75)
    plt.show()
    
    

    
# Data Path for Amazon best buy electronic products
path1 = (r'C:\Users\44755\Downloads\assignment1/' 
+'Amazon_Best_Buy_Electronics.csv')

# Read Data from path1
data1 = pd.read_csv(path1)

# Create a DataFrame object from data
df1 = pd.DataFrame(data1)

# Create an object having number of counts for all brands
product_counts = df1['brand'].value_counts()

# Brands of concern
products = ['Microsoft', "Lenovo", "Sony", "Logitech"];

products_distribution(product_counts, products, 
                      "Best Buy Products on Amazon.com")

# We will use product_counts as data for bar plot
bar_plot_products_count(product_counts, "Electroinc brands counts on Amazon", 
                        "Brands", "Total Products")


# Preparing data for Line Graph

# Dataset: https://www.kaggle.com/datasets/adityasakare/bitcoin-dataset
path2 = (r'C:\Users\44755\Downloads\assignment1/' 
+'Bitcoin_data.csv')

bitcoin_data = pd.read_csv(path2)

# Filter out data for June 2019
bc_june_2019_data = bitcoin_data.loc[bitcoin_data['Date'].str.contains("Jun")                        
                                     & bitcoin_data['Date'].str.contains("2019")]

# Remove duplicate dates
bc_june_2019_data = bc_june_2019_data.drop_duplicates(subset=['Date'])

line_graph(bc_june_2019_data, "Change in Bitcoin price in June 2019")
print(bc_june_2019_data.columns)




















