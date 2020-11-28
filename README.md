# Purwadhika Final Project: Employee Attrition
# Employee Attrition and Its Problem

Employee attrition is a normal cycle in a company where employees decide to leave, such as retirement, resignation, personal health, new opportunities for advance career, not fit with company culture, and other similar reasons. Attrition seemed to be more voluntary and normal because the influences of attrition come from employee itself rather than company. Due to that, attrition always be compared to turnover, which also have similar things but seemed to be more negative.
However, there are some cons with attrition which cause some problem to the company.
- •	Reduction in size or strength of workforce
- •	Remaining job duties can increase the work load for remaining employees
- •	Losing an employee can lead to the loss of all this acquired knowledge, which is not easily replaceable. 
- •	Losing an employee can affect the smooth functioning of a team and lead to productivity losses.
- •	Losing potential employee
- •	Require not small cost for recruitment and training.

# Dataset
Dataset source: The data is from Kaggle (https://www.kaggle.com/vjchoudhary7/hr-analytics-case-study)

# Goals
- Gain insight from the dataset
- To find if there are any factors possibly increase or reduce the level of attrition
- Build macahine learning to predict if an employee will stay or leave from the company

# Model
- Logistic Regression
- Random Forest Classifier
- Gradient Boosting Classifier

# Work Steps:
- Data Preparation:
  - Understanding the dataset
  - Checking information summary about the dataset
  - Checking if there are any duplicated data
  - Checking if there are any inconsistent data value
- Exploratory Data Analysis and Data Visualization:
  - Performing visualization of descriptive statistic from the dataset
  - Gain insight from the descriptive statistic and the visualization
- Feature Engineering:
  - Filling missing value
  - Encode the categorical variables
  = Split data train and data test
- Modelling
  - Train and test the dataset with the models
  - Find for best parameters with Hypermeter Paratuning : GridSearchCV
  - Train and test the dataset with best parameters
 - Result
  - Gradient Boosting has the best evaluation metrics 
  # Model Result:
  ![](images/\Data Science  Purwadhika\Final Project\Final Project fix all AUC ROC 2.png)
  
  
