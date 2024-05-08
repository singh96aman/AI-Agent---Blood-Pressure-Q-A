# Import necessary modules from your package
from helper import *
from constants import Constants
import pandas as pd
import hashlib
from argparse import ArgumentParser

def _load_data_into_db(db, df, collection):
    for i, row in df.iterrows():
        doc_id = row['hash']
        doc = {}
        for c in df.columns:
            if c != 'hash':
                doc[c] = row[c]
        if not db.doc_exists(collection, doc_id):
            db.add_doc(collection, doc_id, doc)

def _load():
    file_list = ['vitals.csv', 'medication.csv']
    db = MongoDB(db_name='patient')
    df_vitals = _load_dataset(file_list[0],)
    _load_data_into_db(db, df_vitals, 'vitals')
    df_medication = _load_dataset(file_list[1])
    _load_data_into_db(db, df_medication, 'medication')
    
    print('Loaded Vitals from CSV. Dims - ', df_vitals.shape)
    print('Loaded Medication from CSV. Dims - ', df_medication.shape)
    return df_vitals, df_medication

def _load_dataset(file):
    df = pd.read_csv('data/'+file)
    
    # Generate random hash for each row
    hashes = []
    for index, row in df.iterrows():
        # Combine all row values to create a unique string
        row_str = ''.join([str(val) for val in row])
        # Generate hash using MD5 algorithm
        hash_value = hashlib.md5(row_str.encode()).hexdigest()
        hashes.append(hash_value)
    
    # Add hash column to DataFrame
    df['hash'] = hashes
    return df

def _run_agent():
    print('Running Agent')
    

def main():
    print('Starting Blood Pressure Q&A Agent...')
    _load()
    _run_agent()

if __name__ == "__main__":
    main()