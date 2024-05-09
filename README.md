# README

## Description
Develop a blood-pressure Q&A agent to answer the following questions based on patients’ vitals and medication data provided

1. Did the patient have Hypertension/Hypotension given blood-pressure records from vitals?

2. Did the patient get the medication order to treat hypertension/hypotension if any?

## Workflow
1. Agent loads data from data folder and saves in DB.
2. Agent then queries OpenAI GPT-4 to with above questions and data retrieved from DB.
3. Agent Responses stored in DB are retrieved and analyze against heuristic logic predictions.

## Submssion
From the Video Submission and Submission Logs, we can see that patient 1 has Hypertension and has been provided with the appropriate medicine.
Patient 2 however has Hypotension has not yet been provided with the appropriate medicine.

## Data and DB
Datasets need to be loaded in `data\___.csv` folder and DB used is MongoDB Atlas (URI in `constants\constants.py`) 
Please add a `.env` file where you can put your `OPENAI_KEY`. Note - OpenAI doesn't allow pushing these keys on Github.

## LLM Agent Templates

All templates are visible [click here](https://github.com/singh96aman/AI-Agent---Blood-Pressure-Q-A/blob/main/src/helper/templates.py)

## Video  and Submission Log

Please see the Video Submission where the Agent runs from Docker container, queries LLM and shows responses against heurstic logic 

Video [click here](https://github.com/singh96aman/AI-Agent---Blood-Pressure-Q-A/blob/main/VideoSubmission.mp4)
Logs [click here](https://github.com/singh96aman/AI-Agent---Blood-Pressure-Q-A/blob/main/submissionlogs.txt)

## Submission Logs

From the submission logs, we can see that Patient