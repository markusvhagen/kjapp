import pandas as pd
import math
import datetime

keep_rows = {1} | set(range(5, 101))
dfMale = pd.read_excel("../data/MaleRoadStd2025.xlsx", sheet_name=1, skiprows=lambda x: x not in keep_rows)
dfFemale = pd.read_excel("../data/FemaleRoadStd2025.xlsx", sheet_name=1, skiprows=lambda x: x not in keep_rows)

gender = input("Enter gender for full list (F=Female, M=Male): ")

df = dfMale if gender=="M" else dfFemale

# 0-indexed indices in excel file: 5k = 2, 10k = 7, HM = 13, M = 16.
# We make a matrix of all the standards
# First index is age, second index is distance, so we index by [age][distance]
# For first index, 0 = 5yrs and so on, for second index 0=5k, 1=10k, 2=HM, 3=M.
for age in range(5,101):
    ageRow5K = df[df["Age"]==age].values.tolist()[0][2]
    ageRow10K = df[df["Age"]==age].values.tolist()[0][7]
    ageRowHM = df[df["Age"]==age].values.tolist()[0][13]
    ageRowM = df[df["Age"]==age].values.tolist()[0][16]
    print("[" + str(ageRow5K) + ", " + str(ageRow10K) + ", " + str(ageRowHM) + ", " + str(ageRowM) + "], ")
