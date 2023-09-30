# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error

# Load the dataset
data = pd.read_csv('housing.csv')

# Display basic statistics of the dataset
data_description = data.describe()
print(data_description)

# Plot histograms for numerical features
data.hist(bins=30, figsize=(15, 10))
plt.show()

# Create a pair plot for selected features
sns.pairplot(data, x_vars=["median_income", "population", "housing_median_age"], y_vars=["median_house_value"], height=4)
plt.show()

# Identify and encode categorical columns
categorical_columns = data.select_dtypes(include=['object']).columns
print("Categorical Columns:", categorical_columns)
data = pd.get_dummies(data, columns=['ocean_proximity'])

# Calculate and visualize correlation matrix
correlation_matrix = data.corr()
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
plt.show()

# Handle missing values
missing_values = data.isnull().sum()
print("Missing Values:\n", missing_values)
data.dropna(inplace=True)
print("Total Rows after Dropping Missing Values:", data.count()[0])

# Scale numerical features using StandardScaler
scaler = StandardScaler()
features_to_scale = ['total_rooms', 'households', 'total_bedrooms', 'population', 'median_house_value']
data[features_to_scale] = scaler.fit_transform(data[features_to_scale])

# Split the dataset into training and testing sets
X = data.drop("median_house_value", axis=1)  # Features (all columns except the target)
y = data["median_house_value"]  # Target variable
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train a linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model using metrics
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)

# Display evaluation results
print("Mean Absolute Error:", mae)
print("Mean Squared Error:", mse)
print("Root Mean Squared Error:", rmse)
