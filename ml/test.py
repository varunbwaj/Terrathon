import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load synthetic data from CSV files
health_records_df = pd.read_csv('health_records.csv')
behavior_logs_df = pd.read_csv('behavior_logs.csv')
food_intake_logs_df = pd.read_csv('food_intake_logs.csv')

# Basic EDA for Health Records Data
print("Health Records Data:")
print(health_records_df.head())
print(health_records_df.describe())

# Visualize distribution of medical conditions
plt.figure(figsize=(8, 6))
sns.countplot(y='Medical History', data=health_records_df)
plt.title('Distribution of Medical Conditions')
plt.xlabel('Count')
plt.ylabel('Medical Condition')
plt.show()

# Basic EDA for Behavior Logs Data
print("\nBehavior Logs Data:")
print(behavior_logs_df.head())
print(behavior_logs_df.describe())

# Visualize frequency of behavior descriptions
plt.figure(figsize=(8, 6))
sns.countplot(y='Behavior Description', data=behavior_logs_df)
plt.title('Frequency of Behavior Descriptions')
plt.xlabel('Count')
plt.ylabel('Behavior Description')
plt.show()

# Basic EDA for Food Intake Logs Data
print("\nFood Intake Logs Data:")
print(food_intake_logs_df.head())
print(food_intake_logs_df.describe())

# Visualize distribution of dietary preferences/restrictions
plt.figure(figsize=(8, 6))
sns.countplot(y='Dietary Preferences/Restrictions', data=food_intake_logs_df)
plt.title('Distribution of Dietary Preferences/Restrictions')
plt.xlabel('Count')
plt.ylabel('Dietary Preferences/Restrictions')
plt.show()
