import pandas as pd
import matplotlib.pyplot as plt
import numpy as nu

file_path = r"C:\Users\jakey\Python_side_project\data set\marketing_sample_for_amazon_com-ecommerce__20200101_20200131__10k_data.csv"
ecom = pd.read_csv(file_path)
print(ecom.head())
print(ecom.info())