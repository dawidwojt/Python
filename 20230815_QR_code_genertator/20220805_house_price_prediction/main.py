# This project focuses on house price determination based on 1970 Boston house prices dataset.
# I've built a model that can provide price estimate based on home's main characteristics, such as"
#   Number of bedrooms
#   Distance to employment centres
#   Neighbourhood - how rich or poor it is
#   Student per teacher in school ratio
# I've divided the code into steps that is relevant while building a model

 %pip install --upgrade plotly #- it is required only when using Google Colab

# Import statements
import pandas as pd
import numpy as np

import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

pd.options.display.float_format = '{:,.2f}'.format

# Loading Data from csv file with index
data = pd.read_csv('boston.csv', index_col=0)

# Basic Data Exploration
data.shape # 506 rows and 14 columns
data.columns # ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'PRICE']
data.head() # first rows
data.tail() # last rows
data.count() #number of rows per column
data.describe() # This command gives more in depth review about each column values, such as count, mean, standard deviation, minimum etc.

# Cleaning data
data.info()
data.duplicated().values.any() # There are no duplicates.
data.isna().values.any() # There are not null vlues.

# Visualisation
  # House price distibution plot with seaborn
sns.displot(data['PRICE'],
            bins=50,
            aspect=2,
            kde=True,
            color='blue')

plt.title(f'1970s Home Values in Boston. Average: ${(1000*data.PRICE.mean()):.6}')
plt.xlabel('Price in 000s')
plt.ylabel('Nr. of Homes')

plt.show()

  #Even though we focus on modelling the price, we can also see how other factors present itself, I for example find house age quite interesting.
  # House age distibution with seaborn
sns.displot(data['AGE'],
            bins=30,
            aspect=2,
            kde=True,
            color='red')

plt.title(f'1970s Home Age. Average: {(1000*data.PRICE.mean()):.6} years old')
plt.xlabel('Houses age')
plt.ylabel('Nr. of Homes')

  # Distance to employment centres
  sns.displot(data.DIS,
            bins=50,
            aspect=2,
            kde=True,
            color='#9061f1') # we can also use color codes if we want to be specific

plt.title(f'Distance to Employment Centres. Average: {(data.DIS.mean()):.2}')
plt.xlabel('Weighted Distance to 5 Boston Employment Centres')
plt.ylabel('Nr. of Homes')

plt.show()

  # Numbr of bedrooms
  sns.displot(data.RM,
            aspect=2,
            kde=True,
            color='#00796b')

plt.title(f'Distribution of Rooms in Boston. Average: {data.RM.mean():.2}')
plt.xlabel('Average Number of Rooms')
plt.ylabel('Nr. of Homes')

plt.show()

  # Rives access
river_access = data['CHAS'].value_counts()

bar = px.bar(x=['No', 'Yes'],
             y=river_access.values,
             color=river_access.values,
             color_continuous_scale=px.colors.sequential.haline,
             title='Is there an access to the river?')

bar.update_layout( yaxis_title='Number of Homes',
                  coloraxis_showscale=False)
bar.show()

# Pairplot
sns.pairplot(data)
plt.show()


# This has shown when to look next to establish relationships:
  # Distance from employment and Nitrix Oxide Pollution - easy to spot that the further away from employment, the NOX is lower
with sns.axes_style('darkgrid'):
  sns.jointplot(x=data['DIS'],
                y=data['NOX'],
                height=8,
                kind='scatter',
                color='brown',
                joint_kws={'alpha':0.5})

plt.show()

  # Non retail industry to NOX - same story - the more factories, the more of NOX
with sns.axes_style('darkgrid'):
  sns.jointplot(x=data.NOX,
                y=data.INDUS,
                # kind='hex',
                height=7,
                color='darkred',
                joint_kws={'alpha':0.5})
plt.show()

  # Proportion of lower income population to number of rooms
with sns.axes_style('darkgrid'):
  sns.jointplot(x=data['LSTAT'],
                y=data['RM'],
                # kind='hex',
                height=7,
                color='orange',
                joint_kws={'alpha':0.5})
plt.show()

  # House price vs low income population
with sns.axes_style('darkgrid'):
  sns.jointplot(x=data.LSTAT,
                y=data.PRICE,
                # kind='hex',
                height=7,
                color='crimson',
                joint_kws={'alpha':0.5})
plt.show()

  #Bedroom numbers vs value of home
with sns.axes_style('whitegrid'):
  sns.jointplot(x=data.RM,
                y=data.PRICE,
                height=7,
                color='darkblue',
                joint_kws={'alpha':0.5})
plt.show()

# Splitting Dataset ito Training and Test Datasets
target = data['PRICE']
features = data.drop('PRICE', axis=1)

X_train, X_test, y_train, y_test = train_test_split(features,
                                                    target,
                                                    test_size=0.2,
                                                    random_state=10)

# % of training set
train_pct = 100*len(X_train)/len(features)
print(f'Training data is {train_pct:.3}% of the total data.')

# % of test data set
test_pct = 100*X_test.shape[0]/features.shape[0]
print(f'Test data makes up the remaining {test_pct:0.3}%.')


# Creating LInear Regression
regr = LinearRegression()
regr.fit(X_train, y_train)
rsquared = regr.score(X_train, y_train)

print(f'Training data r-squared: {rsquared:.2}') # We get 0.75 so that means our R2 is very high, good.

# Next let's examine coefficients

regr_coef = pd.DataFrame(data=regr.coef_, index=X_train.columns, columns=['Coefficient'])
regr_coef

# Premium for having an extra room
premium = regr_coef.loc['RM'].values[0] * 1000  # i.e., ~3.11 * 1000
print(f'The price premium for having an extra room is ${premium:.5}')


predicted_vals = regr.predict(X_train)
residuals = (y_train - predicted_vals)

# Original Regression of Actual vs. Predicted Prices
plt.figure(dpi=100)
plt.scatter(x=y_train, y=predicted_vals, c='indigo', alpha=0.6)
plt.plot(y_train, y_train, color='cyan')
plt.title(f'Actual vs Predicted Prices: $y _i$ vs $\hat y_i$', fontsize=17)
plt.xlabel('Actual prices 000s $y _i$', fontsize=14)
plt.ylabel('Prediced prices 000s $\hat y _i$', fontsize=14)
plt.show()

# Residuals vs Predicted values
plt.figure(dpi=100)
plt.scatter(x=predicted_vals, y=residuals, c='indigo', alpha=0.6)
plt.title('Residuals vs Predicted Values', fontsize=17)
plt.xlabel('Predicted Prices $\hat y _i$', fontsize=14)
plt.ylabel('Residuals', fontsize=14)
plt.show()

# Residual Distribution Chart
resid_mean = round(residuals.mean(), 2)
resid_skew = round(residuals.skew(), 2)

sns.displot(residuals, kde=True, color='indigo')
plt.title(f'Residuals Skew ({resid_skew}) Mean ({resid_mean})')
plt.show()

# Time to think about transforming Data
  #Residuals have skewness of 1.46, so that means there is a lot that can be improved, perhabs using log transformation

tgt_skew = data['PRICE'].skew()
sns.displot(data['PRICE'], kde='kde', color='green')
plt.title(f'Normal Prices. Skew is {tgt_skew:.3}')
plt.show()

y_log = np.log(data['PRICE'])
sns.displot(y_log, kde=True)
plt.title(f'Log Prices. Skew is {y_log.skew():.3}')
plt.show()


plt.figure(dpi=150)
plt.scatter(data.PRICE, np.log(data.PRICE))

plt.title('Mapping the Original Price to a Log Price')
plt.ylabel('Log Price')
plt.xlabel('Actual $ Price in 000s')
plt.show()

  # IT is clear that this is a better fit

# New regression with the use of log prices
new_target = np.log(data['PRICE']) # Use log prices
features = data.drop('PRICE', axis=1)

X_train, X_test, log_y_train, log_y_test = train_test_split(features,
                                                    new_target,
                                                    test_size=0.2,
                                                    random_state=10)

log_regr = LinearRegression()
log_regr.fit(X_train, log_y_train)
log_rsquared = log_regr.score(X_train, log_y_train)

log_predictions = log_regr.predict(X_train)
log_residuals = (log_y_train - log_predictions)

print(f'Training data r-squared: {log_rsquared:.2}')

  #Time to evaluate the coefficients
df_coef = pd.DataFrame(data=log_regr.coef_, index=X_train.columns, columns=['coef'])
df_coef



print(f'Original Model Test Data r-squared: {regr.score(X_test, y_test):.2}')
print(f'Log Model Test Data r-squared: {log_regr.score(X_test, log_y_test):.2}')


  # Average Values in the Dataset
features = data.drop(['PRICE'], axis=1)
average_vals = features.mean().values
property_stats = pd.DataFrame(data=average_vals.reshape(1, len(features.columns)),
                              columns=features.columns)
property_stats


  # Prediction
log_estimate = log_regr.predict(property_stats)[0]
print(f'The log price estimate is ${log_estimate:.3}')

  # Converting Log Prices to Acutal Dollar Values
dollar_est = np.elog_estimate * 1000

  # Define Property Characteristics
next_to_river = True
nr_rooms = 8
students_per_classroom = 20
distance_to_town = 5
pollution = data.NOX.quantile(q=0.75) # high
amount_of_poverty =  data.LSTAT.quantile(q=0.25) # low

  # Property Characteristics
property_stats['RM'] = nr_rooms
property_stats['PTRATIO'] = students_per_classroom
property_stats['DIS'] = distance_to_town

if next_to_river:
    property_stats['CHAS'] = 1
else:
    property_stats['CHAS'] = 0

property_stats['NOX'] = pollution
property_stats['LSTAT'] = amount_of_poverty

  # Prediction
log_estimate = log_regr.predict(property_stats)[0]
print(f'The log price estimate is ${log_estimate:.3}')

  # Converting Log Prices to Acutal Dollar Values
dollar_est = np.e**log_estimate * 1000
print(f'The property is estimated to be worth ${dollar_est:.6}')

#The log price estimate is $3.25
#The property is estimated to be worth $25792.0
