import pandas as pd

BusinessTravel = ['Travel_Rarely','Travel_Frequently','Non-Travel']

Department = ['Sales','Research & Development','Human Resources']

EducationField = ['Life Sciences','Other','Medical' 'Marketing','Technical Degree','Human Resources']

Gender = ['Female','Male']

JobRole =  ['Healthcare Representative', 'Research Scientist', 'Sales Executive',
            'Human Resources', 'Research Director', 'Laboratory Technician',
            'Manufacturing Director', 'Sales Representative', 'Manager']

MaritalStatus = ['Married', 'Single', 'Divorced']

Education = ['Bachelor', 'College', 'Master', 'Below College', 'Doctor']


def data_awal():
    df = pd.read_csv('employeedata.csv')
    return df

def data_awal2():
    df = pd.read_csv('employee_data.csv')
    return df
