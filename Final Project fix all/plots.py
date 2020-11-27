import plotly
import plotly.graph_objects as go
import plotly.express as px
import json
import pandas as pd

from data import data_awal, data_awal2

def pie_dept():
    employee_data = data_awal2()
    department = employee_data['Department'].value_counts()/employee_data['Department'].value_counts().sum() * 100
    department = pd.DataFrame([department.keys(),department.values], index=['Department','DeptPercentage']).T
    fig = px.pie(department, values='DeptPercentage', names='Department', title="Employee's Department Percentage" )
    fig.update_traces(textposition='inside', textinfo='percent+label')
    fig_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return fig_json

def pie_marital():
    employee_data = data_awal2()
    marital = employee_data['MaritalStatus'].value_counts()/employee_data['MaritalStatus'].value_counts().sum() * 100
    marital = pd.DataFrame([marital.keys(),marital.values], index=['MStats','MaritalPct']).T
    fig = px.pie(marital, values='MaritalPct', names='MStats', title="Employee's Marital Status Percentage" )
    fig.update_traces(textposition='inside', textinfo='percent+label')
    fig_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return fig_json

def pie_role():
    employee_data = data_awal2()
    role = employee_data['JobRole'].value_counts()/employee_data['JobRole'].value_counts().sum() * 100
    role = pd.DataFrame([role.keys(),role.values], index=['Role','RolPct']).T
    role
    fig = px.pie(role, values='RolPct', names='Role', title="Employee's Job Role Percentage" )
    fig.update_traces(textposition='inside', textinfo='percent+label')
    fig_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return fig_json

def attrition():
    employee_data = data_awal2()
    attrition = round((employee_data['Attrition'].value_counts()/employee_data['Attrition'].value_counts().sum() * 100), 2)
    attrition = pd.DataFrame(attrition)
    fig = px.pie(attrition, values='Attrition', names=attrition.index, title="Employee's Attrition Percentage" )
    fig.update_traces(textposition='inside', textinfo='percent+label')
    fig_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return fig_json
    

