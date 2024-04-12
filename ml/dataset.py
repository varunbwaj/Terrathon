import pandas as pd
import numpy as np
from faker import Faker
import random
from datetime import datetime, timedelta

# Function to generate synthetic health records data for each patient ID
def generate_health_records(patient_id, num_days):
    fake = Faker()
    health_records = []
    for day in range(num_days):
        for _ in range(3):  # Collect data three times a day
            medical_history = random.choice(['Autism spectrum disorder', 'Epilepsy', 'ADHD', 'Down syndrome'])
            medications = ', '.join([fake.random_element(elements=('Risperidone', 'Valproic acid', 'Lamotrigine', 'Aripiprazole')) for _ in range(random.randint(1, 3))])
            health_assessments = {'Date': (datetime.now() - timedelta(days=day)).strftime('%Y-%m-%d'),
                                  'Physical Health': random.choice(['Stable', 'Unstable']),
                                  'Cognitive Function': random.choice(['Normal', 'Mild impairment', 'Moderate impairment']),
                                  'Emotional Well-being': random.choice(['Stable', 'Elevated anxiety levels', 'Depressed mood'])}
            health_records.append([patient_id, medical_history, medications, *health_assessments.values()])
    return pd.DataFrame(health_records, columns=['Patient ID', 'Medical History', 'Current Medications', 'Date', 'Physical Health', 'Cognitive Function', 'Emotional Well-being'])

# Function to generate synthetic behavior logs data for each patient ID
def generate_behavior_logs(patient_id, num_days):
    fake = Faker()
    behavior_logs = []
    for day in range(num_days):
        for _ in range(3):  # Collect data three times a day
            timestamp = (datetime.now() - timedelta(days=day)).strftime('%Y-%m-%d %H:%M:%S')
            behavior_description = random.choice(['Agitation', 'Restlessness', 'Self-stimulatory behavior', 'Aggression'])
            trigger = random.choice(['Loud noises', 'Crowded environment', 'Change in routine', 'Unfamiliar stimuli'])
            severity_level = random.choice(['Mild', 'Moderate', 'Severe'])
            behavior_logs.append([patient_id, timestamp, behavior_description, trigger, severity_level])
    return pd.DataFrame(behavior_logs, columns=['Patient ID', 'Timestamp', 'Behavior Description', 'Trigger', 'Severity Level'])

# Function to generate synthetic food intake logs data for each patient ID
def generate_food_intake_logs(patient_id, num_days):
    fake = Faker()
    food_intake_logs = []
    for day in range(num_days):
        for _ in range(3):  # Collect data three times a day
            timestamp = (datetime.now() - timedelta(days=day)).strftime('%Y-%m-%d %H:%M:%S')
            food_item = fake.random_element(elements=('Chicken soup', 'Vegetable stir-fry', 'Pasta with marinara sauce', 'Grilled cheese sandwich'))
            quantity = random.randint(1, 2)
            dietary_preferences = random.choice(['No known allergies', 'Gluten-free diet', 'Lactose intolerance'])
            food_intake_logs.append([patient_id, timestamp, food_item, quantity, dietary_preferences])
    return pd.DataFrame(food_intake_logs, columns=['Patient ID', 'Timestamp', 'Food/Fluid Item', 'Quantity', 'Dietary Preferences/Restrictions'])

# Generate synthetic data for health records, behavior logs, and food intake logs for each patient ID
health_records_data = []
behavior_logs_data = []
food_intake_logs_data = []

for patient_id in range(1, 101):  # Assuming 100 patients
    health_records_data.append(generate_health_records(patient_id, 30))
    behavior_logs_data.append(generate_behavior_logs(patient_id, 30))
    food_intake_logs_data.append(generate_food_intake_logs(patient_id, 30))

# Concatenate dataframes for each data type
health_records_df = pd.concat(health_records_data, ignore_index=True)
behavior_logs_df = pd.concat(behavior_logs_data, ignore_index=True)
food_intake_logs_df = pd.concat(food_intake_logs_data, ignore_index=True)

# Save synthetic data to CSV files
health_records_df.to_csv('health_records.csv', index=False)
behavior_logs_df.to_csv('behavior_logs.csv', index=False)
food_intake_logs_df.to_csv('food_intake_logs.csv', index=False)

print("Synthetic data generated and saved to CSV files.")
