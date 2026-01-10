import pandas as pd
import math
import datetime

keep_rows = {1} | set(range(5, 101))
dfMale = pd.read_excel("../data/MaleRoadStd2025.xlsx", sheet_name=1, skiprows=lambda x: x not in keep_rows)
dfFemale = pd.read_excel("../data/FemaleRoadStd2025.xlsx", sheet_name=1, skiprows=lambda x: x not in keep_rows)

gender = input("Enter your gender (F=Female, M=Male): ")
age = int(input("Enter your age: "))
inputDistance = input("Choose a distance to input distance for (5K=5, 10K=10, HM=21, M=42): ")
inputTime = input("Enter your time (H:MM:SS): ")

inputTimeArray = inputTime.split(":")
inputTime = int(inputTimeArray[0])*3600 + int(inputTimeArray[1])*60 + int(inputTimeArray[2])

df = dfMale if gender=="M" else dfFemale

ageRow = df[df["Age"]==age].values.tolist()[0]
print(ageRow)
# 0-indexed indices in excel file: 5k = 2, 10k = 7, HM = 13, M = 16.
ageStandard5K = ageRow[2]
ageStandard10K = ageRow[7]
ageStandardHM = ageRow[13]
ageStandardM = ageRow[16]
ageGrading = 1
if inputDistance=="5":
    ageGrading = ageStandard5K/inputTime
if inputDistance=="10":
    ageGrading = ageStandard10K/inputTime
if inputDistance=="21":
    ageGrading = ageStandardHM/inputTime
if inputDistance=="42":
    ageGrading = ageStandardM/inputTime

equiv5K = str(datetime.timedelta(seconds=math.ceil(ageStandard5K/ageGrading)))
equiv10K = str(datetime.timedelta(seconds=math.ceil(ageStandard10K/ageGrading)))
equivHM = str(datetime.timedelta(seconds=math.ceil(ageStandardHM/ageGrading)))
equivM = str(datetime.timedelta(seconds=math.ceil(ageStandardM/ageGrading)))

print("Your age grading: " + str(ageGrading))
print("5K Equivalent: " + equiv5K)
print("10K Equivalent: " + equiv10K)
print("Half Marathon Equivalent: " + equivHM)
print("Marathon Equivalent: " + equivM)
