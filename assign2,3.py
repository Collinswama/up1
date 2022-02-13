import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go


emp_att = pd.read_csv("https://raw.githubusercontent.com/Collinswama/ADS-Assignment-2-3/main/WA_Fn-UseC_-HR-Employee-Attrition.csv")
emp_att

import plotly.offline as pyo
pyo.init_notebook_mode()

emp_att.describe()

emp_att.columns


plt.rcParams["figure.figsize"] = (15,10)
daf1 = emp_att.groupby(['Attrition', 'JobRole'])['DistanceFromHome'].sum().reset_index()
daf1

fig = sb.stripplot(data = daf1, x = "JobRole", y = "DistanceFromHome", hue = "Attrition")
plt.xlabel = "Job Role"
plt.ylabel = "Commute Distance"
plt.xticks(rotation = 45)

fig

daf2 = emp_att.groupby(["MonthlyIncome", "Education"])["Attrition"].sum().reset_index()
daf2.head(3)

fig2 = sb.barplot(x = daf2.Education, y = daf2.MonthlyIncome, data = daf2, hue = daf2.Attrition)
fig2



