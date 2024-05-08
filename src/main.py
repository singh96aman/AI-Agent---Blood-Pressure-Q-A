# Import necessary modules from your package
from helper import *
from constants import Constants
import pandas as pd
import hashlib
from argparse import ArgumentParser
import warnings

# Suppress warnings
warnings.filterwarnings("ignore")

def _load_data_into_db(db, df, collection):
    for i, row in df.iterrows():
        doc_id = row['hash']
        doc = {}
        for c in df.columns:
            if c != 'hash':
                doc[c] = row[c]
        if not db.doc_exists(collection, doc_id):
            db.add_doc(collection, doc_id, doc)

def _load(db):
    file_list = ['vitals.csv', 'medication.csv']
    df_vitals = _load_dataset(file_list[0],)
    _load_data_into_db(db, df_vitals, 'vitals')
    df_medication = _load_dataset(file_list[1])
    _load_data_into_db(db, df_medication, 'medication')
    
    print('Loaded Vitals from CSV. Dims - ', df_vitals.shape)
    print('Loaded Medication from CSV. Dims - ', df_medication.shape)
    return df_vitals, df_medication

def _load_dataset(file):
    df = pd.read_csv('data/'+file)
    
    hashes = []
    for index, row in df.iterrows():
        row_str = ''.join([str(val) for val in row])
        hash_value = hashlib.md5(row_str.encode()).hexdigest()
        hashes.append(hash_value)
    
    df['hash'] = hashes
    return df

def _run_agent(db):
    agent = Agent(db)
    agent.run_agent()

def _analyze_agent_response(db):
    analysis = Analysis(db)
    analysis.run_analysis()

def main():   
    print('Starting Blood Pressure Q&A Agent...\n\n')
    db = MongoDB(db_name='patient')

    print('\nLoading Data into DB....\n')
    _load(db)

    print('\nRunning LLM Agent...\n\n')
    _run_agent(db)

    print('\nAnalyzing LLM Agent Responses...\n\n')
    _analyze_agent_response(db)

if __name__ == "__main__":
    main()