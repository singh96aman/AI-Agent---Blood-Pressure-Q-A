import pandas as pd
from tabulate import tabulate

class Analysis:
    def __init__(self, db):
        self.db = db

    def _load_patient_data_from_db(self, collection):
        data = pd.DataFrame(self.db.get_all(collection))
        return data

    def getHyperHypoTension(self, df):
        df = df[df["ComponentID"] == "BloodPressure"]
        # Extract systolic and diastolic blood pressure values
        df[['Systolic', 'Diastolic']] = df['ObservationResult'].str.split('/', expand=True)
        df[['Systolic', 'Diastolic']] = df[['Systolic', 'Diastolic']].astype(float)

        # Define function to classify blood pressure
        def classify_blood_pressure(row):
            systolic = row['Systolic']
            diastolic = row['Diastolic']
            if systolic >= 140 or diastolic >= 90:
                return "Hypertension"
            elif systolic < 90 or diastolic < 60:
                return "Hypotension"
            else:
                return "Normal"

        # Apply the function to create a new column indicating blood pressure condition
        df['BloodPressureCondition'] = df.apply(classify_blood_pressure, axis=1)
        return df[["ObservationResult","BloodPressureCondition"]].to_markdown()

    def run_analysis(self):
        vitals = self._load_patient_data_from_db('vitals').drop(columns='_id')
        medication = self._load_patient_data_from_db('medication').drop(columns='_id')
        responses = self._load_patient_data_from_db('responses').drop(columns='_id')
        for pid in vitals['PatientID'].unique():
            pid_vitals = vitals[vitals['PatientID'] == pid]
            pid_medication = medication[medication['PatientID'] == pid]
            pid_responses = responses[responses['PatientID'] == pid]
            pid_responses = pid_responses[pid_responses['Timestamp'] == pid_responses['Timestamp'].min()]['Response'].iloc[0]
            print('\n###########################################\n')
            print('\nPatient ID - ', pid, '\n')
            print('LLM Agent Response - ', pid_responses)
            print('\nHeuristic Logic - \n')
            print(self.getHyperHypoTension(pid_vitals))
            print('\nVitals for Reference - \n')
            print(pid_vitals.to_markdown())
            print('\nMedication for Reference - \n')
            print(pid_medication['ProviderInstructions'].to_markdown())
            