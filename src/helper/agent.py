from collections import defaultdict
import pandas as pd
from .templates import QUESTION1_PROMPT, QUESTION2_PROMPT
from datetime import datetime
import hashlib
from .openaimodel import OpenAIModel

class Agent:

    '''
        Objectives -

        Develop a blood-pressure Q&A agent to answer the following questions based on patients’ vitals and medication data provided

            Did the patient have Hypertension/Hypotension given blood-pressure records from vitals?

            Did the patient get the medication order to treat hypertension/hypotension if any? 

        Requirements -

            You will need to store the vital and medication records to a database you preferred (e.g. MySQL)

            The agent will decide which table to query (vital or medication) and how to query given the corresponding question

            After the corresponding data is retrieved, the agent will answer the two questions with explanations through LLM API

        The dataset includes vital and med records for two patients (p1 and p2). Please ask the two questions for each of the patients in the agent.

        Resources -

            The vital and medication dataset for two patients: See Attachment

            Definition of Hypotension: Hypotension (low blood pressure) is generally considered a blood pressure reading lower than 90 mmHg for the top number (systolic) or 60 mm Hg for the bottom number (diastolic).

            Definition of Hypertension: Hypertension (high blood pressure) is when the pressure in your blood vessels is too high (140/90 mmHg or higher). 

    '''

    def __init__(self, db):
       self.db = db
       self.q1 = QUESTION1_PROMPT.prompt
       self.q2 = QUESTION2_PROMPT.prompt
       self.openai = OpenAIModel()

    def _query_agent(self, df, type):
        for pid in df['PatientID'].unique():
            df_pid = df[df['PatientID'] == pid].drop(['_id', 'PatientID'], axis=1)
            reference_text = df_pid.to_csv(index=False)
            if type == 'vitals':
                pid_q = self.q1.format(reference=reference_text)
            else:
                pid_q = self.q2.format(reference=reference_text)
            pid_q_response = self.openai.predict(pid_q)
            #pid_q_response = 'HyperTension'
            response = {
                'PatientID' : pid,
                'Type' : type,
                'Timestamp': datetime.now(),
                'Prompt' : pid_q,
                'Response' : pid_q_response
            }
            doc_id = hashlib.md5(str(response).encode()).hexdigest()
            self.db.add_doc('responses',doc_id, response)
            #print(pid, pid_q_response)


    def _load_patient_data_from_db(self, collection):
        data = pd.DataFrame(self.db.get_all(collection))
        return data
                    
    def run_agent(self):
        vitals = self._load_patient_data_from_db('vitals')
        medication = self._load_patient_data_from_db('medication')
        self._query_agent(vitals, 'vitals')
        self._query_agent(medication, 'medication')

