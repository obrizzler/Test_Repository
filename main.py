# This is a sample Python script.

# new script
x = "Hi"
print(x)

# Lists
PV = [2.85, 3.30, 3.50, 3.60, 3.85, 4.10, 4.26, 4.55, 4.60, 4.75]
print(PV)
Test = [1,2,3,4]
PVTEST = PV + Test
print(PVTEST)
Item1 = PV[0]
Last_item = PV[-1]
Other = Test[0:2]
print(Item1)
print(Last_item)
print(Other)
print(type(Other))
"""
import libraries
imported packages in PyCharm
"""
import numpy as np
import os
import pandas as pd

# numpy array
PV_array = np.array(PV)
print(type(PV_array))
Item1_int = int(Item1)
Last_item_int = int(Last_item)
print(Item1_int)
print(type(Item1_int))
print(Item1_int, Last_item_int)
PV
print(Test)

# importing dataframe
print(os.getcwd())
os.chdir(r"C:\Users\obria\OneDrive\Documents\Edu\UCD - Data Anlaytics\Data Project")
waiter_tips = pd.read_csv('waiter_tips.csv', encoding = 'ISO-8859-1')
print(waiter_tips.head())
print("Inserting Space Between Tables")
print(waiter_tips.tail())

