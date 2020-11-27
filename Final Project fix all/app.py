from flask import Flask, render_template, request
from data import BusinessTravel, Department, EducationField, Gender, JobRole, MaritalStatus, Education
from prediction import prediction_data
from plots import pie_dept, pie_marital, pie_role, attrition
# inisialisasi Flask
app = Flask(__name__)



#home
@app.route('/')
def home():
    return render_template('home.html')

# EDA
@app.route('/eda')
def eda():
    data = pie_dept()
    marital = pie_marital()
    role = pie_role()
    target = attrition()
    return render_template('eda.html', data=data, marital=marital, role=role, attrition=target)

#prediction
@app.route('/predict', methods=['GET','POST'])
def prediction():
    if request.method == 'POST':
        data = request.form
        data = data.to_dict()
        data['MonthlyIncome'] = int(data['MonthlyIncome'])
        data['NumCompaniesWorked'] = int(data['NumCompaniesWorked'])
        data['Age'] = int(data['Age'])
        data['DistanceFromHome'] = int(data['DistanceFromHome'])
        data['TotalWorkingYears'] = int(data['TotalWorkingYears'])
        data['TrainingTimesLastYear'] = int(data['TrainingTimesLastYear'])
        data['YearsAtCompany'] = int(data['YearsAtCompany'])
        data['YearsSinceLastPromotion'] = int(data['YearsSinceLastPromotion'])
        data['YearsWithCurrManager'] = int(data['YearsWithCurrManager'])
        data['JobLevel'] = int(data['JobLevel'])
        data['StockOptionLevel'] = int(data['StockOptionLevel'])
        data['JobInvolvement'] = int(data['JobInvolvement'])
        data['EnvironmentSatisfaction'] = int(data['EnvironmentSatisfaction'])
        data['JobSatisfaction'] = int(data['JobSatisfaction'])
        data['WorkLifeBalance'] = int(data['WorkLifeBalance'])
        data['PerformanceRating'] = int(data['PerformanceRating'])
        data['PercentSalaryHike'] = int(data['PercentSalaryHike'])


        hasil = prediction_data(data)
        # hasil_pred = []
        # if hasil == 0:
        #     hasil_pred.append('No')
        # elif hasil == 1:
        #     hasil_pred.append('Yes')

        return render_template('result.html', hasil_prediction=hasil)
    return render_template('prediction.html', data_travel=BusinessTravel, data_dept=sorted(Department), 
    data_edu = Education, data_field=sorted(EducationField), data_gender=Gender, data_role=sorted(JobRole), data_marital=MaritalStatus  )

if __name__ == '__main__' :
    app.run(debug=True, port=1111)