import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

url = '/Users/colby/Documents/Lambda/01 Sprint 1/Project/sources/BankChurners.csv'

bank = pd.read_csv(url)

bank = bank[["CLIENTNUM","Attrition_Flag","Customer_Age","Gender","Dependent_count","Education_Level","Marital_Status","Income_Category","Card_Category","Months_on_book","Total_Relationship_Count","Months_Inactive_12_mon","Contacts_Count_12_mon","Credit_Limit","Total_Revolving_Bal","Avg_Open_To_Buy","Total_Amt_Chng_Q4_Q1","Total_Trans_Amt","Total_Trans_Ct","Total_Ct_Chng_Q4_Q1","Avg_Utilization_Ratio"]]

print(bank.describe())