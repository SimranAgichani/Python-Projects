import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
import pickle
# Uncomment the following snippet of code to debug problems with finding the .pkl file path
# This snippet of code will exit the program and print the current working directory.
#import os
#exit(os.getcwd())
own_model = pickle.load(open('C:/Users/simra/Downloads/svm_linear_ownership.pkl', "rb"))
print("\n*****************************************************")
print("* The USF Super Simple Ownership Prediction Model *")
print("*****************************************************\n")
Income = float(input("Enter the income: "))
Lot_Size = float(input("Enter the lot_size: "))
df = pd.DataFrame({'Income': [Income] ,'Lot_Size': [Lot_Size]})


Ownership = own_model.predict(df)
probability = own_model.predict_proba(df)
#owner = ('Not Test', 'Test')
print(f"\nThe USF Simple Ownership model indicates probability of owning a house at {probability[0][1]:.4f}\n")