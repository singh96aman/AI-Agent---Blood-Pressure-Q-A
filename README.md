# README

## Description
Develop a blood-pressure Q&A agent to answer the following questions based on patients’ vitals and medication data provided

1. Did the patient have Hypertension/Hypotension given blood-pressure records from vitals?

2. Did the patient get the medication order to treat hypertension/hypotension if any?

## Workflow
1. Agent loads data from data folder and saves in DB.
2. Agent then queries OpenAI GPT-4 to with above questions and data retrieved from DB.
3. Agent Responses are stored in DB and Users can query AI responses for a given patient ID at their own convenience. 

## Data and DB
Datasets need to be loaded in `data\___.csv` folder and DB used is MongoDB Atlas (URI in `constants\constants.py`) 

## Run Modes
### Run entire Agent Workflow in Default mode
`python main.py`

### Loading Data to DB
`python main.py -l vitals,medication`

### Running BloodPressure Q&A Agent for a given patient ID
`python main.py -r`

### Running BloodPressure Q&A Agent for a given patient ID
patient_id example - p1,p2
`python main.py -r patient_ids`

### Analyze for a given patient IDs
patient_id example - p1,p2
`python main.py -a patient_ids`
